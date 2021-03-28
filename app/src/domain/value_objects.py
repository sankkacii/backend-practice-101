from dataclasses import dataclass


@dataclass(frozen=True)
class PostId:
    value: str

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class PostTitle:
    value: str

    def __post_init__(self):
        if len(self.value) < 1 or len(self.value) > 50:
            raise ValueError("PostTitle 의 값은 1~50자 여야 합니다.")

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class AuthorId:
    value: str

    def __post_init__(self):
        if len(self.value) < 1 or len(self.value) > 30:
            raise ValueError("AuthorId 의 값은 1~30자 여야 합니다.")

    def __str__(self):
        return self.value
