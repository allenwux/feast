import os
import yaml
import logging
import uuid

from abc import ABC, abstractmethod
from datetime import datetime
from proto.v012.feast.core.Registry_pb2 import Registry
from azure.storage.blob import BlobClient
from metadata.repo_config import RepoConfig
from tempfile import TemporaryFile
from errors.errors import FeastInternalServerError

class MetadataServiceFactory():

    @staticmethod
    def GetMetadataService():
        service_type = os.getenv("FEAST_METADATA_SERVICE_TYPE")
        if service_type is None:
            raise FeastInternalServerError(f"Service configuration FEAST_METADATA_SERVICE_TYPE is not set.")

        if service_type == 'blob':
            container_url = os.getenv("FEAST_METADATA_BLOB_CONTAINER_URL")
            sas_key = os.getenv("FEAST_METADATA_BLOB_SAS_KEY")
            if container_url is None:
                raise FeastInternalServerError(f"Service configuration FEAST_METADATA_BLOB_CONTAINER_URL is not set.")
            if sas_key is None:
                raise FeastInternalServerError(f"Service configuration FEAST_METADATA_BLOB_SAS_KEY is not set.")

            return BlobMetadataService(container_url=container_url, sas_key=sas_key)
        else:
            raise FeastInternalServerError(f"Metadata service type {service_type} is not supported.")

class MetadataService(ABC):

    @abstractmethod
    def get_repo_config(self):
        pass

    @abstractmethod
    def get_registry_proto(self):
        pass

    @abstractmethod
    def update_registry_proto(self, registry_proto: Registry):
        pass

class BlobMetadataService(MetadataService):

    def __init__(self, container_url: str, sas_key: str):
        self.container_url = container_url
        self.sas_key = sas_key
        return

    def get_repo_config(self):
        blob_url = f"{self.container_url}/feature_store.yaml{self.sas_key}"
        config_str = self._read_text_from_blob(blob_url)

        raw_config = yaml.safe_load(config_str)
        
        repo_config = RepoConfig(raw_config)
        return repo_config

    def get_registry_proto(self):
        blob_url = f"{self.container_url}/metadata.db{self.sas_key}"
        registry_proto = Registry()
        registry_proto.ParseFromString(self._read_text_from_blob(blob_url))
        return registry_proto

    def update_registry_proto(self, registry_proto: Registry):
        blob_url = f"{self.container_url}/metadata.db{self.sas_key}"
        registry_proto.version_id = str(uuid.uuid4())
        registry_proto.last_updated.FromDatetime(datetime.utcnow())
        proto_str = registry_proto.SerializeToString()
        self._write_text_to_blob(blob_url, proto_str)
        return

    def _read_text_from_blob(self, blob_url: str):
        blob = BlobClient.from_blob_url(blob_url)
        file_obj = TemporaryFile()
        if blob.exists():
            download_stream = blob.download_blob()
            file_obj.write(download_stream.readall())

            file_obj.seek(0)
            return file_obj.read()
        else:
            raise FileNotFoundError(f'Registry not found at path "{self._uri.geturl()}". Have you run "feast apply"?')

    def _write_text_to_blob(self, blob_url: str, content: str):
        blob = BlobClient.from_blob_url(blob_url)
        file_obj = TemporaryFile()
        file_obj.write(content)
        file_obj.seek(0)
        blob.upload_blob(file_obj, overwrite=True)