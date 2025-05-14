from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import todo_routes
from app.services.todo_service import TodoService
import uvicorn
import atexit

import os
import sys
sys.dont_write_bytecode = True

# Create service instance
todo_service = TodoService()

# Clean up __pycache__ folders at startup
todo_service.cleanup_pycache()

app = FastAPI(
    title="Todo App",
    description="A simple Todo application with FastAPI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
todo_service.initialize_database()

# Include routers
app.include_router(todo_routes.router)

# Register cleanup function to run when the application exits
atexit.register(todo_service.cleanup_pycache)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)