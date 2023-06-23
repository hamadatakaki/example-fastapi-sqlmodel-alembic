from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from example_fastapi_sqlmodel_alembic.users.model import User

from sqlmodel import Field, Relationship, SQLModel


class PostBase(SQLModel):
    content: str


class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="posts")
