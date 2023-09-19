from fastapi import Request
from fastapi.responses import JSONResponse

from app.main import app

# from exceptions import CredentialsException, UserAlreadyExistsException


# @app.exception_handler(CredentialsException | UserAlreadyExistsException)
# async def custom_exception_handler(
#         request: Request,
#         exc: CredentialsException | UserAlreadyExistsException
# ):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"error": exc.detail}
#     )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
