from unittest import mock

from application.use_cases.read_post import ReadPost, ReadPostResponse


def test_read_post_success(app, client):
    # given
    read_post_mock = mock.Mock(spec=ReadPost)
    read_post_mock.execute.return_value = ReadPostResponse(
        id="1",
        title="title 1",
        author_id="author 1",
        content="content 1",
        created_at=0,
        updated_at=0,
    )

    # when
    with app.container.read_post.override(read_post_mock):
        response = client.get(
            "/posts/1",
        )

    # then
    assert response.status_code == 200
    assert response.json() == dict(
        id="1",
        title="title 1",
        author_id="author 1",
        content="content 1",
        created_at=0,
        updated_at=0,
    )
