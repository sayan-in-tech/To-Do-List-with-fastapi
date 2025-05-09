from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import todo_routes
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Todo API",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "api_version": "1.0.0"
    }

# Include routers
app.include_router(todo_routes.router)

