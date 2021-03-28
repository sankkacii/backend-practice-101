from pytest import fixture

from application.use_cases.create_post import CreatePost, CreatePostRequest, CreatePostResponse
from domain.entities import Post
from domain.value_objects import PostId, PostTitle, AuthorId


@fixture
def create_post(post_repository):
    return CreatePost(post_repository=post_repository)


def test_create_post_success(create_post, post_repository):
    # given
    request = CreatePostRequest(title="title-1", author_id="author-1", content="content-1")

    # when (1)
    actual = create_post.execute(request)

    # then (1) 출력 값이 맞는지 확인
    expected = CreatePostResponse(
        id="0",
        title="title-1",
        author_id="author-1",
        content="content-1",
        created_at=actual.created_at,
        updated_at=actual.updated_at,
    )
    assert actual == expected

    # when (2)
    actual = post_repository.find_all()

    # then (2) 실제로 업데이트 되어 저장되었는지 확인
    expected = [
        Post(
            id=PostId("0"),
            title=PostTitle("title-1"),
            author_id=AuthorId("author-1"),
            content="content-1",
        )
    ]
    assert actual == expected
