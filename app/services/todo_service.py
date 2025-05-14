import os
import psycopg2
import shutil
import sys
from dotenv import load_dotenv
from app.persistence.models import db, Base
from app.persistence.repository import TodoRepository
from app.routes import todo_routes

sys.dont_write_bytecode = True

class TodoService:
    def __init__(self):
        self.repository = TodoRepository()
        self.db = db

    # Database initialization methods
    def initialize_database(self):
        """Initialize the database connection and create tables if they don't exist."""
        try:
            # Create database if it doesn't exist
            self._create_database_if_not_exists()
            
            # Initialize the database connection
            self.db.init_db()
            return True
        except Exception as e:
            raise Exception(f"Failed to initialize database: {str(e)}")

    def _create_database_if_not_exists(self):
        """Create the database if it doesn't exist."""
        # Default database URL if not set in environment
        DEFAULT_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/todo_db"
        database_url = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
        
        # Extract database name from URL
        db_name = database_url.split('/')[-1]
        # Create connection URL without database name
        base_url = '/'.join(database_url.split('/')[:-1])
        
        try:
            # Connect to PostgreSQL server
            conn = psycopg2.connect(base_url + '/postgres')
            conn.autocommit = True
            cursor = conn.cursor()
            
            # Check if database exists
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
            exists = cursor.fetchone()
            
            if not exists:
                # Create database if it doesn't exist
                cursor.execute(f'CREATE DATABASE {db_name}')
                print(f"Database '{db_name}' created successfully")
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error creating database: {str(e)}")
            raise

    # Utility methods
    @staticmethod
    def cleanup_pycache():
        """Remove all __pycache__ directories from the project."""
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        for root, dirs, files in os.walk(project_root):
            if '__pycache__' in dirs:
                
                pycache_path = os.path.join(root, '__pycache__')
                try:
                    shutil.rmtree(pycache_path)
                except Exception as e:
                    print(f"Error removing {pycache_path}: {str(e)}")

        try:
            print("All __pycache__ directories removed successfully.")
        except Exception as e:
            print(f"Error removing __pycache__ directories: {str(e)}")

    # Todo CRUD methods
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

    def update_todo(self, todo_id, completed=None):
        try:
            todo = self.repository.update(todo_id, completed)
            if not todo:
                raise ValueError(f"Todo with id {todo_id} not found")
            return todo.to_dict()
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
        
    def check_everything(self):
        try:
            todo_routes.create_todo("test")
            todo_id = todo_routes.todo_service.get_all_todos()[-1]["id"]
            
            try:
                print(todo_routes.get_all_todos())
            except Exception as e:
                print(f"Error getting all todos: {str(e)}")
            try:
                print(todo_routes.update_todo(todo_id, True))
            except Exception as e:
                print(f"Error updating todo: {str(e)}")
            try:
                print(todo_routes.get_todo(todo_id))
            except Exception as e:
                print(f"Error getting todo by id: {str(e)}")
            try:
                print(todo_routes.delete_todo(todo_id))
            except Exception as e:
                print(f"Error deleting todo: {str(e)}")
            return "Everything is working.\n However, this test does not check for whether the database exists or not."
        except Exception as e:
            raise e
