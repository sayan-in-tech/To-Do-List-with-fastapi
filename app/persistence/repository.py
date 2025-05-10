from app.persistence.models import db, Todo

class TodoRepository:
    def get_all(self):
        return Todo.query.all()

    def get_by_id(self, todo_id):
        return Todo.query.get(todo_id)

    def create(self, title):
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
        return todo

    def update(self, todo_id, title=None, completed=None):
        todo = self.get_by_id(todo_id)
        if todo:
            if title is not None:
                todo.title = title
            if completed is not None:
                todo.completed = completed
            db.session.commit()
        return todo

    def delete(self, todo_id):
        todo = self.get_by_id(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return todo
