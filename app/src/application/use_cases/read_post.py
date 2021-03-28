from dataclasses import dataclass

from application.use_cases.abstract import UseCase, UseCaseRequest, UseCaseResponse
from domain.repository import PostRepository
from domain.value_objects import PostId


@dataclass
class ReadPostRequest(UseCaseRequest):
    post_id: str


@dataclass
class ReadPostResponse(UseCaseResponse):
    id: str
    title: str
    author_id: str
    content: str
    created_at: int
    updated_at: int


class ReadPost(UseCase):
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, request: ReadPostRequest) -> ReadPostResponse:
        post = self.post_repository.find_by_id(PostId(request.post_id))
        return ReadPostResponse(
            id=str(post.id),
            title=str(post.title),
            author_id=str(post.author_id),
            content=post.content,
            created_at=post.created_at,
            updated_at=post.updated_at,
        )
