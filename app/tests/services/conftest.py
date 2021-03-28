from pytest import fixture

from infrastructure.in_mem_repository import InMemPostRepository


@fixture
def post_repository():
    return InMemPostRepository()
