from abc import ABCMeta, abstractmethod
from typing import List

from domain.entities import Post
from domain.value_objects import PostId


class PostRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_id(self, post_id: PostId) -> Post:
        pass

    @abstractmethod
    def find_all(self) -> List[Post]:
        pass

    @abstractmethod
    def save(self, post: Post) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, post_id: PostId) -> Post:
        pass

    @abstractmethod
    def get_next_identity(self) -> PostId:
        pass
