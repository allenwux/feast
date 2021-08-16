import os
import json
import sys
from datetime import datetime, timedelta
from feast.errors import (
    AzCredentialsError,
)

class TokenFactory():

    access_token = None
    access_token_expire_on = None

    @staticmethod
    def get_access_token():
        if (TokenFactory.access_token is None) or (TokenFactory.access_token_expire_on is None) or (TokenFactory.access_token_expire_on < datetime.utcnow()):
            TokenFactory.access_token, expire_in = TokenFactory._get_new_access_token()
            TokenFactory.access_token_expire_on = datetime.utcnow() + timedelta(seconds=expire_in)
        return TokenFactory.access_token

    @staticmethod
    def _get_new_access_token():
        try:
            import msal
        except ImportError as e:
            from feast.errors import FeastExtrasDependencyImportError

            raise FeastExtrasDependencyImportError("az", str(e))

        # 0. Get basic info from environment variables
        authority = os.getenv("FEAST_AZ_AUTH_AUTHORITY")
        
        if authority is None:
            tenant_id = os.getenv("FEAST_AZ_AUTH_TENANT_ID")
            if tenant_id is not None:
                authority = f"https://login.microsoftonline.com/{tenant_id}"
        
        if authority is None:
            raise AzCredentialsError(
                f"FEAST_AZ_AUTH_AUTHORITY or FEAST_AZ_AUTH_TENANT_ID is required."
            )
        
        client_id = os.getenv("FEAST_AZ_AUTH_CLIENT_ID")

        if (client_id is None):
            raise AzCredentialsError(
                f"FEAST_AZ_AUTH_CLIENT_ID is required."
            )

        scope = f"api://{client_id}/user_impersonation"
        
        spn_client_id = os.getenv("FEAST_AZ_AUTH_SPN_CLIENT_ID")
        spn_client_secret = os.getenv("FEAST_AZ_AUTH_SPN_CLIENT_SECRET")

        if (spn_client_id is not None) and (spn_client_secret is not None):
            # Authenticate with confidential client
            app = msal.ConfidentialClientApplication(
                spn_client_id, authority, spn_client_secret
            )

            result = None

            result = app.acquire_token_for_client(scope, account=None)

            if not result:
                result = app.acquire_token_for_client(scope)


        else:
            # Authenticate with device code flow
            app = msal.PublicClientApplication(
                client_id, authority=authority,
            )

            result = None

            flow = app.initiate_device_flow([scope])
            if "user_code" not in flow:
                raise AzCredentialsError(
                    f"Fail to create device flow. Error {json.dumps(flow, indent=4)}"
                )

            print(flow["message"])
            sys.stdout.flush()
            result = app.acquire_token_by_device_flow(flow)
        
        if ("access_token" in result) and ("expires_in" in result):
            return result["access_token"], result["expires_in"]
        else:
            if "error_description" in result:
                raise AzCredentialsError(
                    result["error_description"]
                )
            else:
                raise AzCredentialsError(
                    str(result["error"])
                )

