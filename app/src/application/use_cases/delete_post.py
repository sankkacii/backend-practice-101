from dataclasses import dataclass

from application.use_cases.abstract import UseCaseRequest, UseCaseResponse, UseCase
from domain.repository import PostRepository
from domain.value_objects import PostId


@dataclass
class DeletePostRequest(UseCaseRequest):
    post_id: str


@dataclass
class DeletePostResponse(UseCaseResponse):
    pass


class DeletePost(UseCase):
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, request: DeletePostRequest) -> DeletePostResponse:
        _ = self.post_repository.delete_by_id(PostId(request.post_id))
        return DeletePostResponse()
