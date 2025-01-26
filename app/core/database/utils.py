from sqlalchemy import Executable, Result
from sqlalchemy.ext.asyncio import AsyncSession

from .postgres import db


def include_session(func):
    async def wrapper(*args, **kwargs):
        if "session" in kwargs:
            return await func(*args, **kwargs)

        async with db.get_session() as session:
            return await func(*args, session=session, **kwargs)
    return wrapper


@include_session
async def execute_query(
    query: Executable,
    commit: bool = False,
    session: AsyncSession = None,
) -> Result:
    result = await session.execute(query)
    if commit:
        await session.commit()
    return result


@include_session
async def add_to_session(
    instance: object,
    commit: bool = True,
    session: AsyncSession = None,
):
    session.add(instance)
    if commit:
        await session.commit()
