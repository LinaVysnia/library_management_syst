from sqlalchemy import  Boolean, Integer, String, event, DateTime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from datetime import datetime, date
from sqlalchemy.sql import func
import bcrypt

class Reader(Base):
    __tablename__ = "readers"

    id:Mapped[int] = mapped_column(primary_key=True)
    card_id_hash : Mapped[str] = mapped_column(String(55), unique=True)
    name:Mapped[str] = mapped_column(String(255))
    surname:Mapped[str] = mapped_column(String(255))
    dob:Mapped[date] = mapped_column(DateTime)
    address : Mapped[str] = mapped_column(String(500))
    phone_num : Mapped[str] = mapped_column(String(55))
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=0)
    added_on : Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), server_default=func.now()) 

    def __str__(self):
        return f"{self.name} {self.surname} {self.id}"

    def set_password(self, password):
        hashed_card_id = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #I've heard salt makes everything better
        self.card_id_hash = hashed_card_id.decode('utf-8')

    def check_password(self, password):
        hashed_input = bcrypt.hashpw(password.encode('utf-8'), self.card_id_hash.encode('utf-8'))
        return hashed_input.decode('utf-8') == self.card_id_hash

    @staticmethod
    def _validate_dob(dob):
        now = datetime.now()
        if not isinstance(dob, date):
            raise ValueError("Datre of birth must be a valid date")
        if dob < 0 or dob > now:
            raise ValueError(f"Publication year must be between 0 and {now}.")
        return dob

@event.listens_for(Reader, 'before_insert')
def before_reader_insert(mapper, connection, target):
    target.dob = Reader._validate_dob(target.dob)

@event.listens_for(Reader, 'before_update')
def before_reader_update(mapper, connection, target):
    target.dob = Reader._validate_dob(target.dob)