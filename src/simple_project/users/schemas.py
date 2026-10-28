from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr


class UserRead(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    username: str
    email: EmailStr
