from abc import ABC, abstractmethod


class AuthUseCase(ABC):
    @abstractmethod
    async def check_email_exists(self, email: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def signup(
        self, name: str, email: str, password: str, password_check: str
    ) -> str:
        raise NotImplementedError

    @abstractmethod
    async def login(self, email: str, password: str) -> str:
        raise NotImplementedError
