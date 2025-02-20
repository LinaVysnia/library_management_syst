import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Reader, Book, librarian

from data.create_dummy_data import create_dummy_data
from UI.login_page_UI import run_login_UI


load_dotenv()  # Load environment variables from .env

DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")


#will create some books if book_data.json or reader_data.json files doen't exist yet
# create_dummy_data()

# run_login_UI()