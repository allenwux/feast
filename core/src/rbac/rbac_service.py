import os
import logging

class RBACService():

    def CanAccess(self, userName: str):
        admins = os.getenv('FEAST_ADMIN_LIST')
        adminList = admins.lower().split(";")
        if userName.lower() in adminList:
            return True
        else:
            logging.error(f"User {userName} has no access to the service.")