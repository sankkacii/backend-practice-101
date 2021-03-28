from starlette.requests import Request
from starlette.responses import JSONResponse

from domain.exceptions import ResourceNotFoundError
from main import app


@app.exception_handler(ResourceNotFoundError)
async def unicorn_exception_handler(request: Request, exc: ResourceNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )
