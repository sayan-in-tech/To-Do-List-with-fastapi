from pydantic import BaseModel
from typing import Optional

import sys
sys.dont_write_bytecode = True

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True