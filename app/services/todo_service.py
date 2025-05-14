from app.persistence.repository import TodoRepository


import sys
sys.dont_write_bytecode = True

class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def get_all_todos(self):
        try:
            todos = self.repository.get_all()
            return [todo.to_dict() for todo in todos]
        except Exception as e:
            raise Exception(f"Failed to get todos: {str(e)}")

    def get_todo(self, todo_id):
        try:
            todo = self.repository.get_by_id(todo_id)
            if not todo:
                raise ValueError(f"Todo with id {todo_id} not found")
            return todo.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Failed to get todo: {str(e)}")

    def create_todo(self, title):
        try:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")
            todo = self.repository.create(title.strip())
            return todo.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Failed to create todo: {str(e)}")

    def update_todo(self, todo_id, title=None, completed=None):
        try:
            todo = self.repository.update(todo_id, title, completed)
            if not todo:
                raise ValueError(f"Todo with id {todo_id} not found")
            return todo.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Failed to update todo: {str(e)}")

    def delete_todo(self, todo_id):
        try:
            todo = self.repository.delete(todo_id)
            if not todo:
                raise ValueError(f"Todo with id {todo_id} not found")
            return todo.to_dict()
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Failed to delete todo: {str(e)}")
