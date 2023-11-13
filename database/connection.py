from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

DATABASE_URL = 'sqlite:///inpost.db'
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()