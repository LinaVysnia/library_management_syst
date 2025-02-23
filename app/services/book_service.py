from app.db import Session
from sqlalchemy import select
from app.models.book import Book
from app.models.history import History
from datetime import datetime
from app.core.const import days_before_overdue

def get_all_books() -> list[Book]:
    with Session() as session:
        stmt = select(Book).where(Book.is_deleted == False)
        all_books = session.execute(stmt).scalars().all()
        return all_books

def print_book_inventory():
    book_obj_list = get_all_books()

    if len(book_obj_list) == 0:
        print("There are no books owned by the library")
    else:
        print(f"There are {len(book_obj_list)} books in the inventory:\n")
        print(f"{'Title':^30}{'Author':^20}{'Publishing year:'}")
        for i, book in enumerate(book_obj_list, 1):
            print(f"{str(i) + '.':<3} {book}")
        print("\n")

def get_available_books() -> list[Book]:
    with Session() as session:
        stmt = select(Book).where(Book.is_borrowed == False).where(Book.is_deleted == False)
        available_books = session.execute(stmt).scalars().all()
        return available_books
        available_books = get_available_books(book_obj_list)

def print_available_books():

    available_books = get_available_books()

    if available_books:
        print(f"There are {len(available_books)} books present in the library:")
        print(f"{'Title':^30}{'Author':^20}{'Publishing year:'}")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. {book}")
        print() 

    else:
        print("All the books in the library are borrowed\n")
  
def get_borrowed_books() -> list[tuple[Book, History]]:
    with Session() as session:
        stmt = select(Book, History).join(History, Book.id == History.book_id).where(Book.is_borrowed == True).where(Book.is_deleted == False)
        borrowed_books = session.execute(stmt).all()
        return borrowed_books

def print_borrowed_books():

    borrowed_books = get_borrowed_books()
    print(borrowed_books)

    if borrowed_books:
        print(f"There are {len(borrowed_books)} books borrowed from the library:")
        print(f"{'Title':<30}{'Author':<20}{'Publishing year:'}")
        for i, (book, history) in enumerate(borrowed_books, 1):
            print(f"{i}. {book}")
            print(f"Borrowed by reader no: {history.reader_id} it has to be returned by {history.due_date}\n")
            if history.due_date < datetime.today():
                print("The book is overdue! The reader won't be able to borrow any more books while the book isn't returned.")
        print()

    else:
        print("No the books are borrowed\n")

def get_overdue_books(reader_id = None) -> list[tuple[Book, datetime]]:

    with Session() as session:
        stmt = (select(Book, History.due_date)
                .join(History, Book.id == History.book_id)
                .where(History.returned_on == None)
                .where(History.due_date < datetime.today())
                .where(Book.is_deleted == False))
        if reader_id:
            stmt = stmt.where(History.reader_id == reader_id)
        overdue_books = session.execute(stmt).all()

    return overdue_books

def print_overdue_books():

    overdue_book_list = get_overdue_books()

    if overdue_book_list:
        print(f"There are {len(overdue_book_list)} book(s) overdue:")
        print(f"{'Title':^30}{'Author':^20}{'Publishing year:'}")
        for i, book, due_date in enumerate(overdue_book_list, 1):
            print(f"{i}. {book}.")
            print(f"Overdue by {((datetime.now() - due_date).days) - days_before_overdue} days\n")
        return

    print("There are no overdue books in the library\n")

def borrow_book(book_id, reader_id, due_date = None):
    with Session() as session:
        book_query = select(Book).where(Book.id == book_id).where(Book.is_borrowed == False)
        book = session.scalars(book_query).one_or_none()

        if not book:
            raise Exception('book is already borrowed or does not exist')
        
        book.is_borrowed = True

        history = History(reader_id = reader_id, book_id = book_id)
        if due_date:
            history.due_date = due_date
        session.add(history)
        
        session.commit()