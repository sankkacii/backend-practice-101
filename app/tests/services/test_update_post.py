from pytest import fixture

from application.use_cases.update_post import UpdatePost, UpdatePostRequest, UpdatePostResponse
from domain.factory import PostFactory
from domain.entities import Post
from domain.value_objects import PostId, PostTitle, AuthorId


@fixture
def update_post(post_repository):
    return UpdatePost(post_repository=post_repository)


def test_update_post_success(update_post, post_repository):
    # given
    post_factory = PostFactory(post_repository)
    post = post_factory.create(title="title-1", author_id="author-1", content="content-1")
    post_repository.save(post)

    # when
    request = UpdatePostRequest(
        id="0", title="title-modified", author_id="author-modified", content="content-modified"
    )
    actual = update_post.execute(request)
    expected = UpdatePostResponse(
        id="0",
        title="title-modified",
        author_id="author-modified",
        content="content-modified",
        created_at=actual.created_at,
        updated_at=actual.updated_at,
    )

    # then (1) 출력 값이 맞는지 확인
    assert actual == expected

    # then (2) 실제로 업데이트 되어 저장되었는지 확인
    actual = post_repository.find_all()
    expected = [
        Post(
            id=PostId("0"),
            title=PostTitle("title-modified"),
            author_id=AuthorId("author-modified"),
            content="content-modified",
        )
    ]
    assert actual == expected
