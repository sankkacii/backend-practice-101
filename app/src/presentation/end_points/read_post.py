from dataclasses import asdict

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse

from application.use_cases.read_post import ReadPostResponse, ReadPost, ReadPostRequest
from container import Container
from presentation.end_points import router


class ReadPostJSONResponseBody(BaseModel):
    id: str
    title: str
    author_id: str
    content: str
    created_at: int
    updated_at: int

    @classmethod
    def from_response(cls, response: ReadPostResponse) -> "ReadPostJSONResponseBody":
        return cls(**asdict(response))


@router.get("/{post_id}")
@inject
def read_post(
    post_id: str,
    use_case: ReadPost = Depends(Provide[Container.read_post]),
) -> JSONResponse:
    request = ReadPostRequest(post_id=post_id)
    response = use_case.execute(request)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=ReadPostJSONResponseBody.from_response(response).dict(),
    )
