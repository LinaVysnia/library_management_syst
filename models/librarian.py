from sqlalchemy import  String, Boolean, DateTime
from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import bcrypt
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

class Librarian(Base):
    __tablename__ = "librarians"

    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(55), unique=True)

    password_hash:Mapped[str] = mapped_column(String(128))

    is_deleted: Mapped[bool] = mapped_column(Boolean, default=0)
    added_on : Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), server_default=func.now())


    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #I've heard salt makes everything better
        self.password_hash = hashed_password.decode('utf-8')

    def check_password(self, password):
        hashed_input = bcrypt.hashpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
        return hashed_input.decode('utf-8') == self.password_hash