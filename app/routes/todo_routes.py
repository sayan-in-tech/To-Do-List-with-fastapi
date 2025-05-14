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
    title: Optional[str] = None
    completed: Optional[bool] = None

@router.get("/")
async def get_todos():
    try:
        return todo_service.get_all_todos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{todo_id}")
async def get_todo(todo_id: int):
    try:
        todo = todo_service.get_todo(todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
async def create_todo(todo: TodoCreate):
    try:
        return todo_service.create_todo(todo.title)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: TodoUpdate):
    try:
        return todo_service.update_todo(todo_id, todo.title, todo.completed)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    try:
        return todo_service.delete_todo(todo_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
