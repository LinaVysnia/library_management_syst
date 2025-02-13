from logic import get_available_books, print_readers, get_readers_overdue_books, print_available_books, borrow_book
from datetime import datetime, timedelta
from const import days_before_overdue
from classes.reader import Reader
from classes.book import Book

def run_book_borrowing_UI(book_obj_list : list , reader_obj_list : list):
    amount_of_readers = len(reader_obj_list)
    available_books =get_available_books(book_obj_list)

    if len(available_books) > 0 and amount_of_readers > 0:

        #letting user to chose which reader borrows a book
        print_readers(reader_obj_list)

        while True:
            user_reader_index_choice = (input(f"Which reader (1 to {amount_of_readers}) wants to borrow a book?: ")).strip()
            try:
                user_reader_index_choice = int(user_reader_index_choice) -1
                if user_reader_index_choice <= (amount_of_readers-1) and user_reader_index_choice >= 0:
                    chosen_readers_overdue_books = get_readers_overdue_books(book_obj_list, reader_obj_list[user_reader_index_choice])
                    if len(chosen_readers_overdue_books) == 0: 
                        break
                    else:
                        print(f"This reader can't borrow because they have {len(chosen_readers_overdue_books)} book(s) overdue:\n")
                        for i, book in enumerate(chosen_readers_overdue_books, 1):
                            print(f"{i}. {book}")
                            print(f"Overdue by {((datetime.now() - book.history[-1][0]).days) - days_before_overdue} days\n")
                        print("Please inform the reader and cho0se somebody else\n")
                else: 
                    print(f"This reader index isn't available. Please make a choice from 1 to {amount_of_readers}\n")
            except:
                print("Your choice isn't valid, pease enter it again\n")

        chosen_reader : Reader = reader_obj_list[user_reader_index_choice]

        print(f"Reader chosen: {chosen_reader}\n")

        #letting user to pick a book from a list
        print_available_books(book_obj_list)
        
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
        reader_cardID = chosen_reader.cardID

        borrow_book(book_obj_list, chosen_book, reader_cardID)

        print(f"{chosen_reader} has successfully borrowed {chosen_book}")
        return_date = (datetime.today() + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
        print(f"it has to be returned by {return_date}\n")
    else:
        print("Unfortunatelly there are no readers registered or all the books are taken, please return at a later date or register a reader\n")

    input("Press enter to return ")