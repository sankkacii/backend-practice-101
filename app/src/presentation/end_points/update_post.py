from dataclasses import asdict

from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse

from application.use_cases.update_post import UpdatePost, UpdatePostRequest, UpdatePostResponse
from container import Container
from presentation.end_points import router


class UpdatePostJSONRequestBody(BaseModel):
    title: str
    author_id: str
    content: str

    def to_request(self, post_id: str) -> UpdatePostRequest:
        return UpdatePostRequest(id=post_id, title=self.title, author_id=self.author_id, content=self.content)


class UpdatePostJSONResponseBody(BaseModel):
    id: str
    title: str
    author_id: str
    content: str
    created_at: int
    updated_at: int

    @classmethod
    def from_response(cls, response: UpdatePostResponse) -> "UpdatePostJSONResponseBody":
        return cls(**asdict(response))


@router.put("/{post_id}")
@inject
def update_post(
    post_id: str,
    request_body: UpdatePostJSONRequestBody,
    use_case: UpdatePost = Depends(Provide[Container.update_post]),
) -> JSONResponse:
    request = request_body.to_request(post_id=post_id)
    response = use_case.execute(request)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=UpdatePostJSONResponseBody.from_response(response).dict(),
    )
