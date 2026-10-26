from fastapi import APIRouter

from simple_project.users.sсhemas import CreateUser
from simple_project.users.crud import create_user as create_user_crud

# from src.simple_project.main import app


router = APIRouter(prefix="/users", tags=["users"])


# используем pydantic-модели BaseModel,
# чтобы клиент отправлял данные json в теле
@router.post("/")
def create_user(user: CreateUser):
    return create_user_crud(user_in=user)
