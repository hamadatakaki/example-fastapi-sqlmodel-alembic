from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from example_fastapi_sqlmodel_alembic.posts.model import Post

from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    family_name: str
    given_name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    posts: List["Post"] = Relationship(back_populates="user")
