from classes.reader import Reader
from UI.book_search_UI import run_book_search_UI
from UI.reader_book_borrowing_UI import run_reader_book_borrowing_UI
from UI.show_readers_borrowed_books import run_show_borrowed_books
from UI.reader_return_borrowed_UI import run_return_book_reader_UI
from logic import *

def run_readers_main_UI(reader : Reader):

    print("*" * 80)
    print(f"Welcome to the library {reader.name}!")
    print("*" * 80, "\n")

    while True:
        print("*" * 80)
        print("Main menu\n")
        print("Please enter the menu item number to select it")
        print(
    """
    1. View library's book inventory
    2. View books present in the library
    3. Search for a book
    4. Borrow a book
    5. Show my borrowed books
    6. Return a book

    Enter "R" to logout and return to the login page

    """)
        user_input = input("Your choice: ").strip()

        if user_input == "1":
                    
            print("*" * 80)
            print("Viewing library's book inventory\n")
            print_inventory(load_books_from_file())
            input("Press enter to return ")

        elif user_input == "2":
            print("*" * 80)
            print("Viewing available books\n")
            print_available_books(load_books_from_file()) 
            input("Press enter to return ")

        elif user_input == "3":
            run_book_search_UI(load_books_from_file())

        elif user_input == "4":
            run_reader_book_borrowing_UI(load_books_from_file(), reader)

        elif user_input == "5":
            run_show_borrowed_books(reader)

        elif user_input == "6":
            run_return_book_reader_UI(reader)

        elif user_input.lower() == "r" or user_input.lower() == "return":
            print("Logging out and returning to the login page")
            break

        else:
            print(f"\"{user_input}\" isn't a valid option, please make another selection")