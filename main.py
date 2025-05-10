from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import todo_routes
import psycopg2
import sqlalchemy
from app.persistence.models import db
import os
from dotenv import load_dotenv
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

@app.on_event("startup")
async def startup():
    db.init(app)

@app.on_event("shutdown")
async def shutdown():
    pass

# Include routers
app.include_router(todo_routes.router)