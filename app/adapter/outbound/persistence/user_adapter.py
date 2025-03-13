from sqlalchemy import select

from app.adapter.outbound.persistence.models import UserModel
from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import UserRepositoryPort
from app.domain import User


class UserPersistenceAdapter(BaseRepository, UserRepositoryPort):
    async def save(self, user: User) -> User:
        model = await self._save(user, UserModel)
        return model.to_domain()

    async def find_by_id_or_none(self, id_: int) -> User | None:
        if model := await self._find_by_id_or_none(id_, UserModel):
            return model.to_domain()

    async def find_by_email(self, email: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        if user := result.scalar_one_or_none():
            return user.to_domain()
