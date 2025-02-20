from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

engine = create_engine(os.environ.get("DATABASE_URL"), echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)