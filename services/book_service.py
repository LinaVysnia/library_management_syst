from db import Session
from sqlalchemy import select
from models.book import Book

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

# def get_overdue_book_list(book_obj_list):

#     def is_overdue(book : Book):

#         if not book.is_borrowed:
#             return False 
#         #book.history[-1][0] gets the latest history entry with [-1] and the time from history item touple with [0]
#         elif (datetime.now() - book.history[-1][0]).days > days_before_overdue: 
#             return True
#         else:
#             return False

#     overdue_book_list = list(filter(lambda book: is_overdue(book), book_obj_list))
#     return overdue_book_list

# def print_overdue_books(book_obj_list):
#     overdue_book_list = get_overdue_book_list(book_obj_list)

#     if len(overdue_book_list) == 0:
#         print("There are no overdue books in the library\n")
#     else:
#         print(f"There are {len(overdue_book_list)} book(s) overdue:")
#         for i, book in enumerate(overdue_book_list, 1):
#             print(f"{i}. {book}.")
#             print(f"Late reader's card ID is : {book.history[-1][1]}")
#             print(f"Overdue by {((datetime.now() - book.history[-1][0]).days) - days_before_overdue} days\n")
