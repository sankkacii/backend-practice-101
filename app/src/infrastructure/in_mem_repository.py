from typing import List

from domain.entities import Post
from domain.exceptions import ResourceNotFoundError
from domain.repository import PostRepository
from domain.value_objects import PostId


class InMemPostRepository(PostRepository):
    def __init__(self) -> None:
        self._posts = {}
        self._next_identity = 0

    def find_by_id(self, post_id: PostId) -> Post:
        try:
            return self._posts[post_id]
        except KeyError:
            raise ResourceNotFoundError(f"존재하지 않는 post_id({post_id}) 입니다.")

    def find_all(self) -> List[Post]:
        return list(self._posts.values())

    def save(self, post: Post) -> None:
        self._posts[post.id] = post

    def delete_by_id(self, post_id: PostId) -> Post:
        try:
            return self._posts.pop(post_id)
        except KeyError:
            raise ResourceNotFoundError(f"존재하지 않는 post_id({post_id}) 입니다.")

    def get_next_identity(self) -> PostId:
        post_id = PostId(str(self._next_identity))
        self._next_identity += 1
        return post_id
