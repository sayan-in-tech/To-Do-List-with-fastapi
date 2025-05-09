# Todo List API with FastAPI

A simple and efficient Todo List API built with FastAPI and SQLAlchemy.

## Features

- Create, read, update, and delete todo items
- Mark todos as complete/incomplete
- Set priorities (Low, Medium, High)
- Add due dates
- Filter todos by completion status and priority
- Pagination support

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Todos

- `POST /todos/` - Create a new todo
- `GET /todos/` - List all todos (with optional filters)
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

### Query Parameters

- `skip`: Number of items to skip (pagination)
- `limit`: Maximum number of items to return (pagination)
- `completed`: Filter by completion status (true/false)
- `priority`: Filter by priority (1: Low, 2: Medium, 3: High)

## Example Usage

### Create a Todo
```bash
curl -X POST "http://localhost:8000/todos/" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Complete project",
           "description": "Finish the todo list project",
           "priority": 2,
           "due_date": "2024-03-20T00:00:00"
         }'
```

### Get All Todos
```bash
curl "http://localhost:8000/todos/"
```

### Update a Todo
```bash
curl -X PUT "http://localhost:8000/todos/1" \
     -H "Content-Type: application/json" \
     -d '{
           "completed": true
         }'
```

### Delete a Todo
```bash
curl -X DELETE "http://localhost:8000/todos/1"
``` 