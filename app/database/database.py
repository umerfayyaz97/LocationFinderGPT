from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

DATABASE_URL = DATABASE_URL

# Creating the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# function to get db session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

