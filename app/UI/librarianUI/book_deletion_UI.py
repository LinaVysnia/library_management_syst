from app.services.book_service import get_all_books, remove_book

def run_book_deletion_UI():
    print("*" * 80)
    print("Removing books from the system\n")

    books = get_all_books()

    print(f"There are {len(books)} books present in the library:")
    print(f"{'Title':^30}{'Author':^20}{'Publishing year:'}")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")

    while True:
        print(f"\nWhich book (1 to {len(books)}) would you like to remove? Enter 'q' to quit.")

        user_input = input("Your choice: ").strip()
        if user_input == "":
            print("Please enter something")
            continue
        else:
            try:
                if user_input.lower() == "q" or user_input.lower() == "quit":
                    print("Quitting removing books")
                    return
                user_input = int(user_input)
                if user_input < 1 or user_input > len(books):
                    print(f"\"{user_input}\" isn't a valid choice. It must be between 1 and {len(books)}")
                    continue
                break

            except:
                print("Something happened that shouldn't have happened")
        
    chosen_book = books[user_input - 1]

    print(f"Are you sere you want to delete this book?")
    print(f"{chosen_book.title} by {chosen_book.author} ({chosen_book.publishing_year})")
    if chosen_book.is_borrowed:
        print("WARNING: This book is currently with a reader!")

    print(
"""
Enter \"y\" for yes
Enter \"n\" for no
Enter \"q\" to quit removing books
""")

    user_choice = input("Your choice: ").lower().strip()
    if user_choice == "y" or user_choice == "yes":
        remove_book(chosen_book)
        print(f"{chosen_book.title} by {chosen_book.author} ({chosen_book.publishing_year}) REMOVED from the library")

    elif user_choice == "n" or user_choice ==  "no":
        print("Deletion cancelled")

    elif user_choice == "q" or user_choice == "quit":
        print("Quitting removing books")
        return
    
    else:
        print(f"{user_choice} isn't a valid choice")


    while True: 

        user_choice = input("\nWould you like yo remove another book? (y/n) : ")
        user_choice = user_choice.strip().lower()

        if user_choice == "n" or user_choice ==  "no":
            print("Quitting removing books")
            return

        elif user_choice == "y" or user_choice ==  "yes":
                
            print("Removing another book...")
            run_book_deletion_UI()
        
        else:
            print(f"Your choice isn't valid please enter only `y` or `n`")
