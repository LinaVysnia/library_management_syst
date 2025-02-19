import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Reader, Book, librarian

from data.create_dummy_data import create_dummy_data
from UI.login_page_UI import run_login_UI


load_dotenv()  # Load environment variables from .env

database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise ValueError("DATABASE_URL environment variable not set. Please create a .env file and set it.")

engine = create_engine(database_url)  # Create the engine *after* loading .env


#will create some books if book_data.json or reader_data.json files doen't exist yet
# create_dummy_data()

# run_login_UI()