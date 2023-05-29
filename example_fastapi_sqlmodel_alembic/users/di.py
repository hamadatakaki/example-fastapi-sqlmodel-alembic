from injector import Binder

from example_fastapi_sqlmodel_alembic.users.usecase import (UserUsecase,
                                                            UserUsecaseImpl)


def users_injector(binder: Binder) -> None:
    binder.bind(UserUsecase, UserUsecaseImpl)
