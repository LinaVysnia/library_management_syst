from app.db import Session
from sqlalchemy import select
from app.models.book import Book
from app.models.history import History
from datetime import datetime
from app.core.const import days_before_overdue

def get_all_books() -> list[Book]:
    with Session() as session:
        stmt = select(Book)
        all_books = session.execute(stmt).scalars().all()
        return all_books

def print_book_inventory():
    book_obj_list = get_all_books()

    if len(book_obj_list) == 0:
        print("There are no books owned by the library")
    else:
        print(f"There are {len(book_obj_list)} books in the inventory:\n")
        for i, book in enumerate(book_obj_list, 1):
            print(f"{str(i) + '.':<3} {book}")
        print("\n")

def get_available_books() -> list[Book]:
    with Session() as session:
        stmt = select(Book).where(Book.is_borrowed == False)
        available_books = session.execute(stmt).scalars().all()
        return available_books
        available_books = get_available_books(book_obj_list)

def print_available_books():

    available_books = get_available_books()

    if available_books:
        print(f"There are {len(available_books)} books present in the library:")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. {book}")
        print() 

    else:
        print("All the books in the library are borrowed\n")
  
def get_borrowed_books() -> list[Book]:
    with Session() as session:
        stmt = select(Book).where(Book.is_borrowed == True)
        borrowed_books = session.execute(stmt).scalars().all()
        return borrowed_books

def print_borrowed_books():

    borrowed_books = get_borrowed_books()

    if borrowed_books:
        print(f"There are {len(borrowed_books)} books borrowed from the library:")
        for i, book in enumerate(borrowed_books, 1):
            print(f"{i}. {book}")
            # return_date = (book.history[-1][0] + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
            # print(f"it has to be returned by {return_date}\n")
        print()

    else:
        print("No the books are borrowed\n")

def get_overdue_books() -> list[(Book, datetime)]:

    with Session() as session:
        stmt = (select(Book, History.due_date)
                .join(History, Book.id == History.book_id)
                .where(History.returned_on == None)
                .where(History.due_date < datetime.today()))
        
        overdue_books = session.execute(stmt).all()

    return overdue_books

def print_overdue_books():

    overdue_book_list = get_overdue_books()

    if overdue_book_list:
        print(f"There are {len(overdue_book_list)} book(s) overdue:")
        for i, book, due_date in enumerate(overdue_book_list, 1):
            print(f"{i}. {book}.")
            print(f"Overdue by {((datetime.now() - due_date).days) - days_before_overdue} days\n")
        return

    print("There are no overdue books in the library\n")