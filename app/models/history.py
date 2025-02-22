from app.models.base import Base

from sqlalchemy import  event, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from typing import Optional

from datetime import datetime, timedelta
from app.core.const import days_before_overdue

class History(Base):
    __tablename__ = "history"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id : Mapped[int] = mapped_column(ForeignKey("books.id"))
    reader_id :Mapped[int] = mapped_column(ForeignKey("readers.id"))
    borrowed_since :Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    due_date : Mapped[datetime] = mapped_column(DateTime)
    returned_on : Mapped[Optional[datetime]] = mapped_column(DateTime)

    book: Mapped["Book"] = relationship("Book", back_populates="borrowing_history") 
    reader: Mapped["Reader"] = relationship("Reader", back_populates="borrowing_history")
    
    def __str__(self):
        return f"book_id={self.book_id}, reader_id={self.reader_id}, borrowed_on={self.borrowed_date}, due_date = {self.due_date}, returned_on={self.returned_date or "Not returned yet"}"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'due_date' not in kwargs:
            self.due_date = self.set_default_due_date()

    def set_default_due_date(self):
        now = datetime.today()
        return_date = now + timedelta(days=days_before_overdue)
        return return_date

    @staticmethod
    def _validate_due_date(due_date):
        now = datetime.today()
        if not isinstance(due_date, datetime):
            raise ValueError("Due date must be a valid date")
        if due_date < now:
            raise ValueError(f"Due date must be later than {now}.")
        return due_date

@event.listens_for(History, 'before_insert')
def before_history_insert(mapper, connection, target):
    target.due_date = History._validate_due_date(target.due_date)

@event.listens_for(History, 'before_update')
def before_history_update(mapper, connection, target):
    target.due_date = History._validate_due_date(target.due_date)