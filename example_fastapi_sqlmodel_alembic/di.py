from injector import Injector

from example_fastapi_sqlmodel_alembic.database.di import database_injector
from example_fastapi_sqlmodel_alembic.users.di import users_injector

modules = [users_injector, database_injector]
injector = Injector(modules)
