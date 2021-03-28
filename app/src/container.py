from dependency_injector import containers, providers

from application.use_cases.create_post import CreatePost
from application.use_cases.delete_post import DeletePost
from application.use_cases.read_post import ReadPost
from application.use_cases.read_posts import ReadPosts
from application.use_cases.update_post import UpdatePost
from infrastructure.in_mem_repository import InMemPostRepository


class Container(containers.DeclarativeContainer):
    post_repository = providers.Singleton(InMemPostRepository)

    create_post = providers.Singleton(CreatePost, post_repository=post_repository)
    delete_post = providers.Singleton(DeletePost, post_repository=post_repository)
    read_posts = providers.Singleton(ReadPosts, post_repository=post_repository)
    read_post = providers.Singleton(ReadPost, post_repository=post_repository)
    update_post = providers.Singleton(UpdatePost, post_repository=post_repository)
