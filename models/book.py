from sqlalchemy import  Column, Integer, String
from models.base import Base

class Book(Base):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    price = db.Column(db.Float, nullable = False)
    picture = db.Column(db.String(255), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    rating = db.Column(db.Integer, default = 0, nullable = True)
    is_available = db.Column(db.Boolean, default = True, nullable = False)
    is_deleted = db.Column(db.Boolean, default = False, nullable = False)
    created_on = db.Column(db.DateTime, default = func.now())

    cart_items = db.relationship("CartItem", back_populates="product")
    order_items = db.relationship("OrderItem", back_populates="product")
    ratings = db.relationship("Rating",back_populates="product")

    def __init__(self, title : str, author : str, publishing_year, genre : str, is_borrowed : bool = False, history :list = []):

        self.title = title
        self.author = author
        self.publishing_year = publishing_year
        self.genre = genre
        self.is_borrowed = is_borrowed
        self.history = history

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.publishing_year})" #return to this and check if  actually used this
    
    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.publishing_year})"
    
    def __eq__(self, other): #this MUST be updated every time class parameters change
        value_comparison = self.title == other.title and self.author == other.author and self.publishing_year == other.publishing_year and self.genre == other.genre and self.is_borrowed == other.is_borrowed and self.history == other.history

        return value_comparison