from logic import *
from classes.librarian import Librarian
from UI.book_search_UI import run_book_search_UI
from UI.register_new_book_UI import run_register_new_book_UI
from UI.old_book_deletion_UI import run_book_deletion_UI
from UI.book_borrowing_UI import run_book_borrowing_UI
from UI.add_reader_UI import run_add_reader_UI
from UI.librarian_returned_borrowed_UI import run_return_book_librarian_UI

def run_librarians_main_UI(librarian : Librarian):

    print("*" * 80)
    print(f"Welcome to the library {librarian.username}!")
    print("*" * 80, "\n")

    while True:
        print("*" * 80)
        print("Main menu\n")
        print("Please enter the menu item number to select it")
        print(
    """
    1. View library's book inventory
    2. View overdue books
    3. View borrowed books
    4. View books present in the library
    5. Search for a book
    6. Register a new book to library's inventory
    7. Delete old books from the system
    8. Lend a book to a reader
    9. Return a book
    10. View all registered readers
    11. Register a new reader

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
            print("Viewing overdue books\n")
            print_overdue_books(load_books_from_file())
            input("Press enter to return ")

        elif user_input == "3":
            print("*" * 80)
            print("Viewing borrowed books\n")
            print_borrowed_books(load_books_from_file()) 
            input("Press enter to return ")
        
        elif user_input == "4":
            print("*" * 80)
            print("Viewing available books\n")
            print_available_books(load_books_from_file()) 
            input("Press enter to return ")

        elif user_input == "5":
            run_book_search_UI(load_books_from_file())

        elif user_input == "6":
            run_register_new_book_UI(load_books_from_file())

        elif user_input == "7":
            run_book_deletion_UI(load_books_from_file())

        elif user_input == "8":
            run_book_borrowing_UI(load_books_from_file(), load_readers_from_file())

        elif user_input == "9":
            run_return_book_librarian_UI()

        elif user_input == "10":
            print("*" * 80)
            print("Viewing all registered users\n")
            print_readers(load_readers_from_file())
            input("Press enter to return ")

        elif user_input == "11":
            run_add_reader_UI(load_readers_from_file())

        elif user_input.lower() == "r" or user_input.lower() == "return":
            print("Logging out and returning to the login page")
            break

        else:
            print(f"\"{user_input}\" isn't a valid option, please make another selection")