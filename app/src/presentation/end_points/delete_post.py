from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from starlette import status
from starlette.responses import JSONResponse

from application.use_cases.delete_post import DeletePost, DeletePostRequest
from container import Container
from presentation.end_points import router


@router.delete("/{post_id}")
@inject
def delete_post(
    post_id: str,
    use_case: DeletePost = Depends(Provide[Container.delete_post]),
) -> JSONResponse:
    request = DeletePostRequest(post_id=post_id)
    _ = use_case.execute(request)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
