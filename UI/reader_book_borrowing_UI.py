from logic import get_available_books, print_readers, get_readers_overdue_books, print_available_books, borrow_book
from datetime import datetime, timedelta
from const import days_before_overdue
from classes.reader import Reader
from classes.book import Book

def run_reader_book_borrowing_UI(book_obj_list : list , reader):
    available_books =get_available_books(book_obj_list)

    if len(available_books) > 0 :

        while True:

            chosen_readers_overdue_books = get_readers_overdue_books(book_obj_list, reader)
            if len(chosen_readers_overdue_books) != 0: 
                print(f"You can't borrow because you have {len(chosen_readers_overdue_books)} book(s) overdue:\n")
                for i, book in enumerate(chosen_readers_overdue_books, 1):
                    print(f"{i}. {book}")
                    print(f"Overdue by {((datetime.now() - book.history[-1][0]).days) - days_before_overdue} days\n")
                print("You must return overdue books before you can borrow again\n")
                break

            #letting user to pick a book from a list
            print_available_books(book_obj_list)
        
            user_book_index_choice = (input(f"Which book (1 to {len(available_books)}) would you like to borrow?: ")).strip()
            try: 
                user_book_index_choice = int(user_book_index_choice) -1
                if user_book_index_choice > (len(available_books)-1) or user_book_index_choice < 0:
                    print("Such a book isn't available. Please make a choice again\n")
                    continue
            except:
                print("Your choice isn't valid, pease enter it again\n")

            chosen_book : Book = available_books[user_book_index_choice]
            reader_cardID = reader.cardID

            borrow_book(book_obj_list, chosen_book, reader_cardID)

            print(f"You have successfully borrowed {chosen_book}")
            return_date = (datetime.today() + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
            print(f"it has to be returned by {return_date}\n")
            break
        
    else:
        print("Unfortunatelly all the books are taken, please return at a later date\n")

    input("Press enter to return ")