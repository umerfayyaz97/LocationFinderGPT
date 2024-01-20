from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import  SessionLocal, engine, Todo

app: FastAPI = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()