from fastapi import APIRouter
from typing import Annotated

from fastapi import Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from simple_project.core.db_helper import db_helper
from simple_project.users.crud import create_user as create_user_crud
from simple_project.users.schemas import CreateUser, UserRead

# from src.simple_project.main import app


router = APIRouter(prefix="/users", tags=["users"])
SessionDep = Annotated[AsyncSession, Depends(db_helper.session_dependency)]


# используем pydantic-модели BaseModel,
# чтобы клиент отправлял данные json в теле
@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, session: SessionDep):
    return await create_user_crud(session=session, user_in=user)
