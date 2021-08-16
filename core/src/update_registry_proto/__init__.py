import logging
import base64
import json

import azure.functions as func
from proto.v012.feast.core.Registry_pb2 import Registry
from rbac.rbac_service import RBACService
from services.registry_service import RegistryService


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    user_name = req.headers["X-MS-CLIENT-PRINCIPAL-NAME"]
    rbac_service = RBACService()
    if not rbac_service.CanAccess(user_name):
        return func.HttpResponse(status_code=403)

    req_body = req.get_json()
    registry_base64_str = req_body['registry']
    registry_bytes = base64.b64decode(registry_base64_str.encode('ascii'))
    registry_service = RegistryService()
    registry_proto = Registry()
    registry_proto.ParseFromString(registry_bytes)

    registry_service.update_registry_proto(registry_proto)
    return func.HttpResponse(json.dumps({"message": "Registry is updated successfully."}))
