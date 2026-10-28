from sqlalchemy.ext.asyncio import AsyncSession

from simple_project.models.user import User
from simple_project.users.schemas import CreateUser


async def create_user(session: AsyncSession, user_in: CreateUser) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
