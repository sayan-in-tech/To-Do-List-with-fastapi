from sqlalchemy import Column, Integer, String
from .database import Base

import sys
sys.dont_write_bytecode = True

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)