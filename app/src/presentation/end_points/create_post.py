from dataclasses import asdict

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse

from application.use_cases.create_post import CreatePost, CreatePostRequest, CreatePostResponse
from container import Container
from presentation.end_points import router


class CreatePostJSONRequestBody(BaseModel):
    title: str
    author_id: str
    content: str

    def to_request(self) -> "CreatePostRequest":
        return CreatePostRequest(title=self.title, author_id=self.author_id, content=self.content)


class CreatePostJSONResponseBody(BaseModel):
    id: str
    title: str
    author_id: str
    content: str
    created_at: int
    updated_at: int

    @classmethod
    def from_response(cls, response: CreatePostResponse) -> "CreatePostJSONResponseBody":
        return cls(**asdict(response))


@router.post("/")
@inject
def create_posts(
    request_body: CreatePostJSONRequestBody,
    use_case: CreatePost = Depends(Provide[Container.create_post]),
) -> JSONResponse:
    request = request_body.to_request()
    response = use_case.execute(request)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=CreatePostJSONResponseBody.from_response(response).dict(),
    )
