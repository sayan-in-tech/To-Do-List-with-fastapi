from app.persistence.models import db, Todo


import sys
sys.dont_write_bytecode = True

class TodoRepository:
    def get_all(self):
        return db.session.query(Todo).order_by(Todo.created_at.desc()).all()
        
    def get_by_id(self, todo_id):
        return db.session.query(Todo).get(todo_id)
    
    def create(self, title):
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    def update(self, todo_id, completed=None):
        todo = db.session.query(Todo).get(todo_id)
        if not todo:
            return None
        
        if completed is not None:
            todo.completed = completed
        
        db.session.commit()
        return todo
    
    def delete(self, todo_id):
        todo = db.session.query(Todo).get(todo_id)
        if not todo:
            return None
        
        db.session.delete(todo)
        db.session.commit()
        return todo