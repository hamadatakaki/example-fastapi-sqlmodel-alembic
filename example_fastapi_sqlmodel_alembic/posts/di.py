from injector import Binder

from example_fastapi_sqlmodel_alembic.posts.usecase import (PostUsecase,
                                                            PostUsecaseImpl)


def users_injector(binder: Binder) -> None:
    binder.bind(PostUsecase, PostUsecaseImpl)
