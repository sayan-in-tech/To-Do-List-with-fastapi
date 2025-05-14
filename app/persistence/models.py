from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from dotenv import load_dotenv

import sys
sys.dont_write_bytecode = True

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Database:
    def __init__(self):
        self._engine = None
        self._session_factory = None
        self._session = None

    def init_db(self):
        load_dotenv()
        # Default database URL if not set in environment
        DEFAULT_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/todo_db"
        database_url = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
        
        self._engine = create_engine(database_url)
        self._session_factory = sessionmaker(bind=self._engine)
        self._session = scoped_session(self._session_factory)
        Base.metadata.create_all(self._engine)

    @property
    def session(self):
        if self._session is None:
            self.init_db()
        return self._session

db = Database()
    