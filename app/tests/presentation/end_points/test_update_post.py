from unittest import mock

from application.use_cases.update_post import UpdatePost, UpdatePostResponse
from presentation.end_points.update_post import UpdatePostJSONRequestBody, UpdatePostJSONResponseBody


def test_update_post_success(app, client):
    # given
    update_post_mock = mock.Mock(spec=UpdatePost)
    update_post_mock.execute.return_value = UpdatePostResponse(
        id="1",
        title="this is title",
        author_id="heumsi",
        content="this is content",
        created_at=1,
        updated_at=1,
    )

    # when
    with app.container.update_post.override(update_post_mock):
        response = client.put(
            "/posts/1",
            json=UpdatePostJSONRequestBody(
                title="this is title",
                author_id="heumsi",
                content="this is content",
            ).dict(),
        )

    # then
    assert response.status_code == 200
    assert (
        response.json()
        == UpdatePostJSONResponseBody(
            id="1",
            title="this is title",
            author_id="heumsi",
            content="this is content",
            created_at=1,
            updated_at=1,
        ).dict()
    )
