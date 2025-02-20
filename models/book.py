from sqlalchemy import  Boolean, Integer, String, event, DateTime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from sqlalchemy.sql import func

from datetime import datetime

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    publishing_year : Mapped[int] = mapped_column(Integer)
    genre: Mapped[str] = mapped_column(String(255))
    is_borrowed: Mapped[bool] = mapped_column(Boolean, default=0)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=0)
    added_on : Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), server_default=func.now())

#might not need these methods, check later
    def __repr__(self):
        return f"{self.title} by {self.author} ({self.publishing_year})" #return to this and check if  actually used this
    
    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.publishing_year})"
    
    def __eq__(self, other): #this MUST be updated every time class parameters change.. bit inefficient
        value_comparison = self.title == other.title and self.author == other.author and self.publishing_year == other.publishing_year and self.genre == other.genre and self.is_borrowed == other.is_borrowed and self.history == other.history

        return value_comparison
    
    @staticmethod
    def _validate_publication_year(year):
        current_year = datetime.now().year
        if not isinstance(year, int):
            raise ValueError("Publication year must be an integer.")
        if year < 0 or year > current_year:
            raise ValueError(f"Publication year must be between 0 and {current_year}.")
        return year

@event.listens_for(Book, 'before_insert')
def before_book_insert(mapper, connection, target):
    target.publication_year = Book._validate_publication_year(target.publication_year)

@event.listens_for(Book, 'before_update')
def before_book_update(mapper, connection, target):
    target.publication_year = Book._validate_publication_year(target.publication_year)