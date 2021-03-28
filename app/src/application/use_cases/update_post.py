import time
from dataclasses import dataclass

from application.use_cases.abstract import UseCase, UseCaseResponse, UseCaseRequest
from domain.entities import Post
from domain.repository import PostRepository
from domain.value_objects import PostId, PostTitle, AuthorId


@dataclass
class UpdatePostRequest(UseCaseRequest):
    id: str
    title: str
    author_id: str
    content: str


@dataclass
class UpdatePostResponse(UseCaseResponse):
    id: str
    title: str
    author_id: str
    content: str
    created_at: int
    updated_at: int


class UpdatePost(UseCase):
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def execute(self, request: UpdatePostRequest) -> UpdatePostResponse:
        post = self.post_repository.find_by_id(PostId(request.id))
        post = Post(
            id=post.id,
            title=PostTitle(request.title),
            author_id=AuthorId(request.author_id),
            content=request.content,
            created_at=post.created_at,
            updated_at=int(time.time()),
        )
        self.post_repository.save(post)
        return UpdatePostResponse(
            id=str(post.id),
            title=str(post.title),
            author_id=str(post.author_id),
            content=post.content,
            created_at=post.created_at,
            updated_at=post.updated_at,
        )
