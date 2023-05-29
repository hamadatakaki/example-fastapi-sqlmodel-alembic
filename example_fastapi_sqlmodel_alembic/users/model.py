from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    family_name: str
    given_name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
