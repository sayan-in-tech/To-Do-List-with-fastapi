from fastapi import APIRouter, HTTPException
from app.services.todo_service import TodoService
from typing import List, Optional
from pydantic import BaseModel

import sys
sys.dont_write_bytecode = True

router = APIRouter(prefix="/todos", tags=["todos"])
todo_service = TodoService()

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    completed: bool = None

@router.get("/check_everything")
async def check_everything():
    return todo_service.check_everything()

@router.get("/get_all_todos")
async def get_all_todos():
    return todo_service.get_all_todos()

@router.get("/{todo_id}")
async def get_todo(todo_id: int):
    todo = todo_service.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/")
async def create_todo(todo: TodoCreate):
    return todo_service.create_todo(todo.title)

@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: TodoUpdate):
    return todo_service.update_todo(todo_id, todo.completed)

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    return todo_service.delete_todo(todo_id)
