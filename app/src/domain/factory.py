from domain.entities import Post
from domain.repository import PostRepository
from domain.value_objects import PostTitle, AuthorId


class PostFactory:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def create(self, title: str, author_id: str, content: str) -> Post:
        return Post(
            id=self.post_repository.get_next_identity(),
            title=PostTitle(title),
            author_id=AuthorId(author_id),
            content=content,
        )
