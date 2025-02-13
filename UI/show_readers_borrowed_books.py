from logic import get_readers_overdue_books, get_borrowed_books, load_books_from_file
from classes.reader import Reader
from datetime import datetime, timedelta
from const import days_before_overdue

def run_show_borrowed_books(reader : Reader):
    print("*" * 80)
    print("Viewing borrowed books\n")
    all_borrowed_books = get_borrowed_books(load_books_from_file())
    readers_borrowed_books = list(filter(lambda book: True if book.history[-1][1] == reader.cardID else False, all_borrowed_books))

    if len(readers_borrowed_books) == 0:
        print("You haven't borrowed any books yet\n")
    
    else:
        overdue_books = get_readers_overdue_books(all_borrowed_books, reader)
        if len(overdue_books) != 0:
            print(f"You have {len(overdue_books)} overdue books!")
            for i, book in enumerate(overdue_books, 1):
                print(f"{i}. {book}")
                print(f"Overdue by {((datetime.now() - book.history[-1][0]).days) - days_before_overdue} days\n")
            print("You must return overdue books before you can borrow again!\n")
        
        print(f"You currently have borrowed {len(readers_borrowed_books)} books:\n")
        for i, book in enumerate(readers_borrowed_books, 1):
            print(f"{i}. {book}")
            return_date = (book.history[-1][0] + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
            print(f"it has to be returned by {return_date}\n")
            print()


    input("Press enter to return ")