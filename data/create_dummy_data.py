import os
from sqlalchemy import select
from db import Session
from models.book import Book
from models.reader import Reader
from models.librarian import Librarian
from const import book_data_path, reader_data_path, librarian_data_path
from datetime import datetime

def create_book_data(dummy_books):
    """
    Creates dummy book data if nothing is present in the table
    """
    with Session() as session:
        stmt = select(Book)
        books_found = session.execute(stmt).first()

        if books_found:
            print(f"At least one book found. Dummy data creation is skipped")
            return

    print(f"No books were found. Initialising dummy data")

    for book in dummy_books:
        try:
            dum_book = Book(
                title = book["title"],
                author = book["author"],
                publishing_year = book["publishing_year"],
                genre = book["genre"],
            )
            stmt = session.add(dum_book)
        except Exception as e:
            print(f"Book addition failed! Book in question: \n{book}")
            print(e)

    session.commit()

def create_reader_data(dummy_readers):
    """
    Creates dummy reader data if nothing is present in the table
    """ 
    with Session() as session:
        stmt = select(Reader)
        readers_found = session.execute(stmt).first()

        if readers_found:
            print(f"At least one reader found. Dummy data creation is skipped")
            return

    print(f"No readers were found. Initialising dummy data")

    for reader in dummy_readers:
        try:
            dum_reader = Reader(
                card_id = reader["cardID"],
                name = reader["name"],
                surname = reader["surname"],
                dob = datetime.strptime(reader["dob"], "%Y %m %d").date(),
                address = reader["address"],
                phone_num = reader["phone_num"]
            )
            stmt = session.add(dum_reader)
        except Exception as e:
            print(f"Reader addition failed! Reader in question: \n{reader}")
            print(e)

    session.commit()

def create_librarian_data(dummy_librarians):
    """
    Creates dummy librarian data if nothing is present in the table
    """
    with Session() as session:
        stmt = select(Librarian)
        libs_found = session.execute(stmt).first()

        if libs_found:
            print(f"At least one librarian found. Dummy data creation is skipped")
            return

    print(f"No librarians were found. Initialising dummy data")

    for lib in dummy_librarians:
        try:
            dum_librarian = Librarian(
                username = lib["username"],
                psw = lib["password"]
            )
            stmt = session.add(dum_librarian)
        except Exception as e:
            print(f"Librarian addition failed! Librarian in question: \n{lib}")
            print(e)

        session.commit()


def create_dummy_data():
   #these are the 10 dummy books to fill the book database
    books = [
        {"title": "To Kill a Mockingbird", 
            "author": "Harper Lee", 
            "publishing_year": 1960, 
            "genre": "Fiction"},

        {"title": "1984", 
            "author": "George Orwell", 
            "publishing_year": 1949, 
            "genre": "Dystopian"},

        {"title": "Pride and Prejudice", 
            "author": "Jane Austen", 
            "publishing_year": 1813, 
            "genre": "Romance"},

        {"title": "The Great Gatsby", 
            "author": "F. Scott Fitzgerald", 
            "publishing_year": 1925, 
            "genre": "Fiction"},

        {"title": "Moby Dick", 
            "author": "Herman Melville", 
            "publishing_year": 1851, 
            "genre": "Adventure"},

        {"title": "War and Peace", 
            "author": "Leo Tolstoy", 
            "publishing_year": 1869, 
            "genre": "Historical Fiction"},

        {"title": "The Hobbit", 
            "author": "J.R.R. Tolkien", 
            "publishing_year": 1937, 
            "genre": "Fantasy"},

        {"title": "Brave New World", 
            "author": "Aldous Huxley", 
            "publishing_year": 1932, 
            "genre": "Dystopian"},

        {"title": "The Catcher in the Rye", 
            "author": "J.D. Salinger", 
            "publishing_year": 1951, 
            "genre": "Fiction"},

        {"title": "The Alchemist", 
            "author": "Paulo Coelho", 
            "publishing_year": 1988, 
            "genre": "Philosophical Fiction"}
    ]

    readers = [
        {
            "name": "Frodo",
            "surname": "Baggins",
            "dob": "1995 09 22",
            "address": "12 Bag End, Hobbiton, Shire",
            "phone_num": "555-123-4567",
            "cardID": "FR0D0B4GG1"
        },
        {
            "name": "Arwen",
            "surname": "Undmiel",
            "dob": "1988 06 15",
            "address": "15 Evenstar Lane, Rivendell",
            "phone_num": "555-987-6543",
            "cardID": "4RW3NUND0M"
        },
        {
            "name": "Geralt",
            "surname": "of Rivia",
            "dob": "1990 04 10",
            "address": "3 Kaer Morhen Drive, Rivia",
            "phone_num": "555-345-6789",
            "cardID": "G3R4LT0FRV"
        },
        {
            "name": "Lyra",
            "surname": "Silvertongue",
            "dob": "2000 12 07",
            "address": "22 Jordan College Way, Oxford",
            "phone_num": "555-567-8901",
            "cardID": "LYR4S1LVRT"
        },
        {
            "name": "Jon",
            "surname": "Snow",
            "dob": "1994 01 16",
            "address": "Castle Black, The Wall, North",
            "phone_num": "555-789-0123",
            "cardID": "J0NSN0WC4S"
        }
    ]

        #a couple of librarians to fill the book database
    
    librarians = [
        {"username": "admin", 
            "password": "Linai 10"},

        {"username": "Lina", 
            "password": "Man 10"}
    ]
    
    create_book_data(books)
    create_reader_data(readers)
    create_librarian_data(librarians)