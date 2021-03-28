from unittest import mock

from application.use_cases.delete_post import DeletePost, DeletePostResponse


def test_delete_post_success(app, client):
    # given
    delete_post_mock = mock.Mock(spec=DeletePost)
    delete_post_mock.execute.return_value = DeletePostResponse()

    # when
    with app.container.delete_post.override(delete_post_mock):
        response = client.delete(
            "/posts/1",
        )

    # then
    assert response.status_code == 204
