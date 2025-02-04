import logging
import base64
import json
import os

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

    registry_service = RegistryService()
    registry_proto = registry_service.get_registry()
    return func.HttpResponse(registry_proto)
