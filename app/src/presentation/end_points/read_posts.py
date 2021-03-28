from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from starlette import status
from starlette.responses import JSONResponse

from application.use_cases.read_posts import ReadPosts, ReadPostsRequest
from container import Container
from presentation.end_points import router
from presentation.end_points.read_post import ReadPostJSONResponseBody


@router.get("/")
@inject
def read_posts(use_case: ReadPosts = Depends(Provide[Container.read_posts])) -> JSONResponse:
    request = ReadPostsRequest()
    response = use_case.execute(request)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=[ReadPostJSONResponseBody.from_response(response).dict() for response in response.items],
    )
