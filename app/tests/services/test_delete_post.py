from pytest import fixture

from application.use_cases.delete_post import DeletePost, DeletePostRequest, DeletePostResponse
from domain.factory import PostFactory


@fixture
def delete_post(post_repository):
    return DeletePost(post_repository=post_repository)


def test_delete_post_success(delete_post, post_repository):
    # given
    post_factory = PostFactory(post_repository)
    post = post_factory.create(title="title-1", author_id="author-1", content="content-1")
    post_repository.save(post)

    # when
    request = DeletePostRequest(
        post_id="0",
    )
    actual = delete_post.execute(request)
    expected = DeletePostResponse()

    # then (1) 출력 값이 맞는지 확인
    assert actual == expected

    # then (2) 실제로 업데이트 되어 저장되었는지 확인
    actual = post_repository.find_all()
    expected = []
    assert actual == expected
