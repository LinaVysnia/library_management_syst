from app.db import Session
from sqlalchemy import select
from app.services.book_service import get_overdue_books
from app.models.reader import Reader
from app.models.book import Book

def get_all_readers() -> list[Reader]:
    with Session() as session:
        stmt = select(Reader).where(Reader.is_deleted == False)
        readers = session.execute(stmt).scalars().all()

    return readers

def print_readers():
    readers = get_all_readers()

    if readers:
        print(f"There are {len(readers)} readers registered at this library: ")
        print(f"{'Name':^15}{'Surname':^20}{'Reader no:'}")
        for i, reader in enumerate(readers, 1):
            print(f"{i}. {reader}")
        return

    print("There are no registered readers at the library")

def get_readers_overdue_books(reader):
    get_readers_overdue_books()
    with Session() as session:
        stmt = select(Book).join()