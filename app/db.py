from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ.get("DATABASE_URL"), echo=False) #change echo True for query printing

Session = sessionmaker(bind=engine)