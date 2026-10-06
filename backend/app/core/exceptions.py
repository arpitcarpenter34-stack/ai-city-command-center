from fastapi import HTTPException


class ResourceNotFoundError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=404, detail={'status': 'error', 'error_code': 'RESOURCE_NOT_FOUND', 'message': message})


class ValidationError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail={'status': 'error', 'error_code': 'VALIDATION_ERROR', 'message': message})


class ConflictError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=409, detail={'status': 'error', 'error_code': 'CONFLICT', 'message': message})
