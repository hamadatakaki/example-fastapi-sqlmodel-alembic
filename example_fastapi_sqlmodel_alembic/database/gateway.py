from abc import ABC, abstractmethod
from contextlib import contextmanager

from sqlmodel import Session, create_engine


class DatabaseGateway(ABC):
    @abstractmethod
    def open_session(self):
        pass


class SQLiteGateway(DatabaseGateway):
    def __init__(self):
        self.engine = create_engine("sqlite:///database.db", echo=True)

    @contextmanager
    def open_session(self):
        yield Session(self.engine)
