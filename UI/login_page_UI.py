from UI.librarian_login_UI import run_librarian_login_UI
from UI.reader_login_UI import run_reader_login_UI

def run_login_UI():
    print("*" * 80)
    print("Welcome to your Library App!")
    print("*" * 80, "\n")

    while True:
        print("*" * 80)
        print("Please login as a librarian or reader")
        print(
    """
    1. Login as librarian
    2. Login as reader

    Enter "Q" to quit the app
    """)

        user_input = input("Your choice: ").strip()

        if user_input == "1":      
            run_librarian_login_UI()

        elif user_input == "2":
            run_reader_login_UI()
            pass

        elif user_input == "q":
            print("Library app is shutting down")
            break

        else:
            print(f"\"{user_input}\" isn't a valid option, please make another selection")