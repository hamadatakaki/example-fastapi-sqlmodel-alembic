from abc import ABC, abstractmethod
from typing import List

from injector import inject
from sqlmodel import select

from example_fastapi_sqlmodel_alembic.database.gateway import DatabaseGateway
from example_fastapi_sqlmodel_alembic.users.model import (User, UserCreate,
                                                          UserRead)


class UserUsecase(ABC):
    @abstractmethod
    def create(self, params: UserCreate) -> UserRead:
        pass

    @abstractmethod
    def read_all(self) -> List[UserRead]:
        pass


class UserUsecaseImpl(UserUsecase):
    @inject
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self.database_gateway = database_gateway

    def create(self, params: UserCreate) -> UserRead:
        user = User.from_orm(params)
        with self.database_gateway.open_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)

        if user.id is None:
            raise Exception("User.id is None.")

        return user

    def read_all(self) -> List[UserRead]:
        with self.database_gateway.open_session() as session:
            stmt_read_all = select(User)
            result = session.exec(stmt_read_all)

        return list(result)
