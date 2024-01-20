from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import  Base, SessionLocal, engine, Todo

app: FastAPI = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

