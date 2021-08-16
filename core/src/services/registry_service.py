from proto.v012.feast.core.Registry_pb2 import Registry
from metadata.metadata_service import BlobMetadataService

class RegistryService:

    def __init__(self):
        self.metadata_service = BlobMetadataService()
        return

    def get_repo_config(self):
        return self.metadata_service.get_repo_config()

    def get_registry_proto(self):
        return self.metadata_service.get_registry_proto()

    def update_registry_proto(self, registry_proto: Registry):
        self.metadata_service.update_registry_proto(registry_proto)
        return
