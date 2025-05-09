from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate
from typing import List, Optional
from datetime import datetime

class TodoService:
    @staticmethod
    def create_todo(db: Session, todo: TodoCreate) -> Todo:
        db_todo = Todo(**todo.model_dump())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    def get_todos(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        completed: Optional[bool] = None,
        priority: Optional[int] = None
    ) -> List[Todo]:
        query = db.query(Todo)
        
        if completed is not None:
            query = query.filter(Todo.completed == completed)
        if priority is not None:
            query = query.filter(Todo.priority == priority)
            
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
        return db.query(Todo).filter(Todo.id == todo_id).first()

    @staticmethod
    def update_todo(db: Session, todo_id: int, todo: TodoUpdate) -> Optional[Todo]:
        db_todo = TodoService.get_todo(db, todo_id)
        if not db_todo:
            return None

        update_data = todo.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_todo, field, value)

        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    def delete_todo(db: Session, todo_id: int) -> bool:
        db_todo = TodoService.get_todo(db, todo_id)
        if not db_todo:
            return False

        db.delete(db_todo)
        db.commit()
        return True 