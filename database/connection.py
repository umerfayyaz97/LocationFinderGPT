from sqlalchemy import Engine, create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy import delete


conn_str = "postgresql://eternitywatches212:CZ4bUW6nVYyQ@ep-blue-sunset-a1zn4ibt.ap-southeast-1.aws.neon.tech/FASTAPI?sslmode=require"

engine: Engine = create_engine(conn_str, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
# db: Session = Session()
# Base.metadata.create_all(bind=engine)

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

   
    