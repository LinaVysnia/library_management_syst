from app.services.book_service import get_available_books, get_overdue_books, print_available_books, borrow_book
from app.services.reader_service import get_all_readers, print_readers
from datetime import datetime, timedelta
from app.core.const import days_before_overdue
from app.models.reader import Reader
from app.models.book import Book

def run_book_borrowing_UI():
    readers = get_all_readers()
    available_books = get_available_books()

    if available_books and readers:

        #letting user to chose which reader borrows a book
        print_readers()

        while True:
            reader_index = (input(f"Which reader (1 to {len(readers)}) wants to borrow a book?: ")).strip()
            try:
                reader_index = int(reader_index) -1

                if reader_index <= (len(readers))-1 and reader_index >= 0:
                    reader = readers[reader_index]
                    overdue_books = get_overdue_books(reader.id)

                    if overdue_books:
                        print(f"This reader can't borrow because they have {len(overdue_books)} book(s) overdue:\n")
                        for i, book in enumerate(overdue_books, 1):
                            print(f"{i}. {book}")
                            print(f"Overdue by {((datetime.now() - book.history[-1][0]).days) - days_before_overdue} days\n")
                        print("Please inform the reader and choose somebody else\n")
                        continue
                    
                    break
                        
                else:
                    print(f"This reader index isn't available. Please make a choice from 1 to {len(readers)}\n")
                    
            except Exception as ex:
                print("Your choice isn't valid, pease enter it again\n")
                print(ex)

        chosen_reader : Reader = readers[reader_index]

        print(f"Reader chosen: {chosen_reader.name} {chosen_reader.surname} reader no. {chosen_reader.id}\n")

        #letting user to pick a book from a list
        print_available_books()
        
        while True:
            user_book_index_choice = (input(f"Which book (1 to {len(available_books)}) would {chosen_reader.name} like to borrow?: ")).strip()
            try: 
                user_book_index_choice = int(user_book_index_choice) -1
                if user_book_index_choice <= (len(available_books)-1) and user_book_index_choice >= 0:
                    break
                else: print("Such a book isn't available. Please make a choice again\n")
            except:
                print("Your choice isn't valid, pease enter it again\n")

        chosen_book : Book = available_books[user_book_index_choice]

        borrow_book(chosen_book.id, chosen_reader.id)

        print(f"{chosen_reader.name} {chosen_reader.surname} reader no. {chosen_reader.id} has successfully borrowed {chosen_book.print_unformatted()})")
        return_date = (datetime.today() + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
        print(f"it has to be returned by {return_date}\n")
    else:
        print("Unfortunatelly there are no readers registered or all the books are taken, please return at a later date or register a reader\n")

    input("Press enter to return ")