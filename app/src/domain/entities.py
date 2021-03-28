import time
from dataclasses import dataclass, field

from domain.value_objects import PostId, PostTitle, AuthorId


@dataclass(eq=False)
class Post:
    id: PostId
    title: PostTitle
    author_id: AuthorId
    content: str
    created_at: int = field(default_factory=lambda: int(time.time()))
    updated_at: int = field(default_factory=lambda: int(time.time()))

    def __eq__(self, other):
        return self.id == other.id
