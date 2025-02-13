from logic import delete_books_older_than
from datetime import datetime

def run_book_deletion_UI(book_obj_list):
    print("*" * 80)
    print("Removing old books from the system\n")
    continue_trying_to_delete = True

    while continue_trying_to_delete:
        while True:
            print("At what age (years) should the books be removed from the system?: ")
            user_input = input("Your choice: ").strip()

            if user_input == "":
                print("Please enter something")
            else:
                try:
                    user_input = int(user_input)
                    age = user_input
                    break
                except:
                    print(f"\"{user_input}\" isn't a valid age")

        current_year = datetime.now().year
        is_book_too_old = lambda book : True if current_year - book.publishing_year > age else False
        old_book_list = list(filter(is_book_too_old, book_obj_list))

        if len(old_book_list) == 0 :
            print(f"There are no books older than {age} years\n")
            while True:
                print("Would you like to try removing old books again with a different age?")
                print(
    """
Enter \"y\" for yes
Enter \"q\" to quit deleting old books
    """)
                user_choice = input("Your choice: ").lower().strip()
                if user_choice == "y" or user_choice == "yes":
                    print("Trying again with a different age\n")
                    break
                elif user_choice == "q" or user_choice == "quit":
                    print("Quitting removing books")
                    continue_trying_to_delete = False
                    break
                else:
                    print(f"{user_choice} isn't a valid choice")
        
        else:
            print(f"There are {len(old_book_list)} books older than {age} years: ")
            for i, book in enumerate(old_book_list, 1):
                print(f"{i}. {book}")

            #forcing the user to make a valid choice 
            while True: 
                user_deletion_choice = input("\nAre you sure you want to permanently delete them from the system? (y/n) : ")
                user_deletion_choice = user_deletion_choice.strip().lower()

                if user_deletion_choice == "n" or user_deletion_choice ==  "no":
                    print("Deletion cancelled")
                    continue_trying_to_delete = False
                    break

                elif user_deletion_choice == "y" or user_deletion_choice ==  "yes":
                        
                        delete_books_older_than(book_obj_list, age)
                        print(f"{len(old_book_list)} books were deleted from the inventory\n")
                        continue_trying_to_delete = False
                        break
                
                else:
                    print(f"Your choice isn't valid please enter only `y` or `n`")
 
    input("Press enter to return ")