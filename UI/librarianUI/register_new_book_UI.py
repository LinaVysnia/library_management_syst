from logic import add_book
from datetime import date

def run_register_new_book_UI(book_obj_list):
    continue_adding_books = True

    while continue_adding_books:
        print("*" * 80)
        print("Registering a new book to library's inventory\n")

        def print_book_progress (title = "?", author = "?", publishing_year = "?", genre = "?"):
            print(
    f"""
New book information:
Title - "{title}"
Author - {author}
Publishing year - {publishing_year}
Genre - {genre}
    """)
        
        print("Please enter the required information")
        print_book_progress()

        while True:
            title = input("Enter the title (without quotation marks): " ).strip()
            if title != "":
                break
            else:
                print("Please enter something")
        
        print_book_progress(title)

        while True:
            author = input("Enter the author of the book: " ).strip()
            if author != "":
                break
            else:
                print("Please enter something")
        
        print_book_progress(title, author)

        while True:
            publishing_year = input("Enter the publishing year as YYYY: " ).strip()
            if publishing_year == "":
                print("Please enter something")

            else:
                try:
                    publishing_year = int(publishing_year)            
                    if publishing_year > date.today().year:
                        print("Unfortunatelly, due to potential liabilities, library doesn't except books from the future")
                    elif publishing_year < 800:
                        print("Such an ancient book should be in a museum. You probably entered the year wrong")
                    else:
                        break
                except:
                    print(f"\"{publishing_year}\" isn't a valid year")
        
        print_book_progress(title, author, publishing_year)
        
        while True:
            genre = input("Enter the genre: " ).strip().lower()
            if genre != "":
                break
            else:
                print("Please enter something")

        while True:
            print("*" * 80)
            print_book_progress(title, author, publishing_year, genre)
            print("Would you like to add this book to the library's inventory?")
            print(
    """
Enter \"y\" for yes
Enter \"r\" to restart
Enter \"q\" to quit adding the new book
    """)
            user_choice = input("Your choice: ").lower().strip()
            if user_choice == "y" or user_choice == "yes":
                add_book(book_obj_list, title, author, publishing_year, genre)
                continue_adding_books = False
                break
            elif user_choice == "r" or user_choice == "restart":
                print("Restarting\n")
                break
            elif user_choice == "q" or user_choice == "quit":
                print("Quitting adding books")
                continue_adding_books = False
                break
            else:
                print(f"{user_choice} isn't a valid choice")
                
    input("Press enter to return ")
        
