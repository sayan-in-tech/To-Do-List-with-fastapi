from app.persistence.repository import TodoRepository

class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def get_all_todos(self):
        todos = self.repository.get_all()
        return [todo.to_dict() for todo in todos]

    def get_todo(self, todo_id):
        todo = self.repository.get_by_id(todo_id)
        return todo.to_dict() if todo else None

    def create_todo(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        todo = self.repository.create(title)
        return todo.to_dict()

    def update_todo(self, todo_id, title=None, completed=None):
        todo = self.repository.update(todo_id, title, completed)
        if not todo:
            raise ValueError(f"Todo with id {todo_id} not found")
        return todo.to_dict()

    def delete_todo(self, todo_id):
        todo = self.repository.delete(todo_id)
        if not todo:
            raise ValueError(f"Todo with id {todo_id} not found")
        return todo.to_dict()
