from unittest import mock

from application.use_cases.read_posts import ReadPosts, ReadPostsResponse


def test_read_posts_success(app, client):
    # given
    read_posts_mock = mock.Mock(spec=ReadPosts)
    read_posts_mock.execute.return_value = ReadPostsResponse(
        items=[
            ReadPostsResponse.Item(
                id="1",
                title="title 1",
                author_id="author 1",
                content="content 1",
                created_at=0,
                updated_at=0,
            ),
            ReadPostsResponse.Item(
                id="2",
                title="title 2",
                author_id="author 2",
                content="content 2",
                created_at=0,
                updated_at=0,
            ),
        ]
    )

    # when
    with app.container.read_posts.override(read_posts_mock):
        response = client.get(
            "/posts/",
        )

    # then
    assert response.status_code == 200
    print(response.json())
    assert response.json() == [
        dict(
            id="1",
            title="title 1",
            author_id="author 1",
            content="content 1",
            created_at=0,
            updated_at=0,
        ),
        dict(
            id="2",
            title="title 2",
            author_id="author 2",
            content="content 2",
            created_at=0,
            updated_at=0,
        ),
    ]
