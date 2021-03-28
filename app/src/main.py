import uvicorn
from fastapi import FastAPI
from starlette import status

from container import Container
from presentation import end_points


def create_app() -> FastAPI:
    container = Container()
    container.wire(packages=[end_points])

    app = FastAPI()
    app.container = container
    app.include_router(end_points.router)
    return app


app = create_app()


@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {"msg": "I'm health!"}


#
# @app.get(
#     "/",
#     responses={
#         status.HTTP_200_OK: {
#             # 아래가 되는거
#             "headers": {
#                 "hello": "",
#             },
#             # "headers": {
#             #     "model": ReadPostsJSONResponseHeader,
#             # },
#             # "headers": ReadPostsJSONResponseHeader.dict(),
#             "model": ReadPostsJSONResponseBody,
#             # "headers": {
#             #     "hello": "world",
#             # },
#         }
#     },
#     # responses={
#     #     201: {
#     #         "headers": {
#     #             "Location": "",
#     #         },
#     #     }
#     # }
#     # status_code=status.HTTP_200_OK,
#     # response_model=ReadPostsJSONResponseBody,
#     # response_class=ReadPostsJSONResponse,
#     # responses={},
# )
# @inject
# def read_posts(service: ReadPosts = Depends(Provide[Container.read_posts])):
#     # request = ReadPostsRequest()
#     # response = service.execute(request)
#     # return ReadPostsJSONResponse.from_response(response)
#     return JSONResponse(headers={"X-hello": "world"}, content={"message": "Hello World"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
