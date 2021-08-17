import base64
import json
from proto.v012.feast.core.Registry_pb2 import Registry
from metadata.metadata_service import MetadataServiceFactory

class RegistryService:

    def __init__(self):
        self.metadata_service = MetadataServiceFactory.GetMetadataService()
        return

    def get_repo_config(self):
        repo_config = self.metadata_service.get_repo_config()
        return json.dumps(repo_config.__dict__)

    def get_registry(self):
        registry_proto = self.metadata_service.get_registry_proto().SerializeToString()
        registry_proto_base64_str = base64.b64encode(registry_proto).decode('utf-8')
        return json.dumps({"registry": str(registry_proto_base64_str)})

    def update_registry_proto(self, requestBody):
        registry_base64_str = requestBody['registry']
        registry_bytes = base64.b64decode(registry_base64_str.encode('ascii'))
        registry_proto = Registry()
        registry_proto.ParseFromString(registry_bytes)
        self.metadata_service.update_registry_proto(registry_proto)
        return
