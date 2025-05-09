from datetime import datetime
from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    priority: int = Field(default=1, ge=1, le=3)
    due_date: datetime | None = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: int | None = Field(default=None, ge=1, le=3)
    due_date: datetime | None = None

class Todo(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True 