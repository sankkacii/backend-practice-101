from unittest import mock

from application.use_cases.create_post import CreatePost, CreatePostResponse
from presentation.end_points.create_post import CreatePostJSONResponseBody, CreatePostJSONRequestBody


def test_create_post_success(app, client):
    # given
    create_post_mock = mock.Mock(spec=CreatePost)
    create_post_mock.execute.return_value = CreatePostResponse(
        id="1", title="this is title", author_id="heumsi", content="this is content", created_at=1, updated_at=1
    )

    # when
    with app.container.create_post.override(create_post_mock):
        response = client.post(
            "/posts/",
            json=CreatePostJSONRequestBody(
                title="this is title", author_id="heumsi", content="this is content"
            ).dict(),
        )

    # then
    assert response.status_code == 201
    assert (
        response.json()
        == CreatePostJSONResponseBody(
            id="1", title="this is title", author_id="heumsi", content="this is content", created_at=1, updated_at=1
        ).dict()
    )
