from typing import List

from fastapi import APIRouter

from example_fastapi_sqlmodel_alembic.di import injector
from example_fastapi_sqlmodel_alembic.users.model import UserCreate, UserRead
from example_fastapi_sqlmodel_alembic.users.usecase import UserUsecase

router = APIRouter()
user_usecase = injector.get(UserUsecase)


@router.post("/api/v1/users/", response_model=UserRead)
async def create_user(param: UserCreate) -> UserRead:
    user = user_usecase.create(param)
    return user


@router.get("/api/v1/users/", response_model=List[UserRead])
async def read_all_user() -> List[UserRead]:
    users = user_usecase.read_all()
    return users
