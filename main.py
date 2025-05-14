from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import todo_routes
import psycopg2
from sqlalchemy import create_engine
from app.persistence.models import db, Base
import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys
sys.dont_write_bytecode = True

load_dotenv()

app = FastAPI(
    title="Todo App",
    description="A simple Todo application with FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable not set")
try:
    # Connect to the PostgreSQL database
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    db.Base.metadata.create_all(bind=engine)
except Exception as e:
    raise Exception(f"Failed to connect to the database: {str(e)}")

app.include_router(todo_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)