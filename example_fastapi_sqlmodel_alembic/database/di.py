from injector import Binder

from example_fastapi_sqlmodel_alembic.database.gateway import (DatabaseGateway,
                                                               SQLiteGateway)


def database_injector(binder: Binder) -> None:
    binder.bind(DatabaseGateway, SQLiteGateway)
