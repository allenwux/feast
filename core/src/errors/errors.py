class FeastInternalServerError(Exception):
    def __init__(self, error_message: str):
        super().__init__(
            f"The service can not process the request. Error Message: {error_message}"
        )