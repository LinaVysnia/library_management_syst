from sqlalchemy import  Boolean, Integer, String, event, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from typing import Optional

from app.models.base import Base
from app.models.history import History

from datetime import datetime

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    publishing_year : Mapped[int] = mapped_column(Integer)
    genre: Mapped[str] = mapped_column(String(255))
    is_borrowed: Mapped[bool] = mapped_column(Boolean, default=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    added_on : Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), server_default=func.now())

    borrowing_history:Mapped[list["History"]] = relationship("History", back_populates="book")

    def print_unformatted(self):
        return f"{self.title} by {self.author} ({self.publishing_year})" #return to this and check if  actually used this
    
    def __str__(self):
        return f"{self.title[:30]:<30} {self.author[:20]:<20} {self.publishing_year:^6}"
    
    
    @staticmethod
    def _validate_publishing_year(year):
        current_year = datetime.now().year
        if not isinstance(year, int):
            raise ValueError("publishing year must be an integer.")
        if year < 0 or year > current_year:
            raise ValueError(f"publishing year must be between 0 and {current_year}.")
        return year

@event.listens_for(Book, 'before_insert')
def before_book_insert(mapper, connection, target):
    target.publishing_year = Book._validate_publishing_year(target.publishing_year)

@event.listens_for(Book, 'before_update')
def before_book_update(mapper, connection, target):
    target.publishing_year = Book._validate_publishing_year(target.publishing_year)