from fastapi import HTTPException, status


class BookingsExceptions(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class CredentialsException(BookingsExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Could not validate credentials'


class UserAlreadyExistsException(BookingsExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = 'User already exists'
