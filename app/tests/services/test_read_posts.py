from pytest import fixture

from application.use_cases.read_posts import ReadPosts, ReadPostsRequest, ReadPostsResponse
from domain.factory import PostFactory
from domain.entities import Post
from domain.value_objects import PostId, PostTitle, AuthorId


@fixture
def read_posts(post_repository):
    return ReadPosts(post_repository=post_repository)


def test_read_posts_success(read_posts, post_repository):
    # given
    post_factory = PostFactory(post_repository)
    posts = [
        post_factory.create(title="title-1", author_id="author-1", content="content-1"),
        post_factory.create(title="title-2", author_id="author-2", content="content-2"),
    ]
    for post in posts:
        post_repository.save(post)

    # when
    request = ReadPostsRequest()
    actual = read_posts.execute(request)
    expected = ReadPostsResponse(items=[ReadPostsResponse.Item.from_entity(post) for post in posts])

    # then 출력 값이 맞는지 확인
    assert actual == expected
