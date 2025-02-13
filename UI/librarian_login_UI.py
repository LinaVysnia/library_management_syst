from logic import load_librarians_from_file
from UI.librarians_main_UI import run_librarians_main_UI

def run_librarian_login_UI():
    all_librarians = load_librarians_from_file()

    print("*" * 80)
    print("Librarian login")

    while True:
        print("Please enter the username or \"l\" to return to the login page")
        username_input = input("Username: ").strip()

        matched_username_librarian = None

        if username_input == "":
            print("Please enter something")

        elif username_input.lower() == "l":
            print("returning to the login page")
            break

        else: 

            for librarian in all_librarians:
                if librarian.username == username_input:
                    print(f"User \"{username_input}\" found")
                    matched_username_librarian = librarian

        if matched_username_librarian != None: 

            while True:
                print("Please enter the password or \"r\" to return to user selection")
                password_input = input("Password: ").strip()

                if password_input.lower() == "r":
                    print("returning to username input")
                    break
                
                else:
                    password_matched = matched_username_librarian.check_password(password_input)
                    if password_matched:
                        print("Password matched!\n")
                        return run_librarians_main_UI(matched_username_librarian)
                    else:
                        print("Password incorrect. Try again")
        else:
            print("Such username doesn't exist. Please try again")
   


