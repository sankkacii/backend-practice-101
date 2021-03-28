from dataclasses import dataclass

from application.use_cases.abstract import UseCaseRequest, UseCaseResponse, UseCase
from domain.factory import PostFactory
from domain.repository import PostRepository


@dataclass
class CreatePostRequest(UseCaseRequest):
    title: str
    author_id: str
    content: str


@dataclass
class CreatePostResponse(UseCaseResponse):
    id: str
    title: str
    author_id: str
    content: str
    created_at: int
    updated_at: int


class CreatePost(UseCase):
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository
        self._post_factory = PostFactory(post_repository=post_repository)

    def execute(self, request: CreatePostRequest) -> CreatePostResponse:
        post = self._post_factory.create(title=request.title, author_id=request.author_id, content=request.content)
        self.post_repository.save(post)
        return CreatePostResponse(
            id=str(post.id),
            title=str(post.title),
            author_id=str(post.author_id),
            content=post.content,
            created_at=post.created_at,
            updated_at=post.updated_at,
        )
