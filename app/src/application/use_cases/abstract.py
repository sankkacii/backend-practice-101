from abc import ABCMeta, abstractmethod
from typing import Optional


class UseCaseRequest(metaclass=ABCMeta):
    pass


class UseCaseResponse(metaclass=ABCMeta):
    pass


class UseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, request: UseCaseRequest) -> Optional[UseCaseResponse]:
        pass
