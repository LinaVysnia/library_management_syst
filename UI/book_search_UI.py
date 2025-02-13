from logic import get_books_by_title, get_books_by_author, get_books_by_publishing_year, get_books_by_genre

def run_book_search_UI(book_ibj_list):

    while True:
        print("*" * 80)
        print("Searching for a book\n")
        print("You can search books by title, author, publishing year or genre")
        user_choice = input("""
    \"t\" to search by title 
    \"a\" to search by author
    \"p\" to search by publishing year 
    \"g\" to search by genre
    or \"q\" to quit searching
                            
please enter your selection: """)
        user_choice = user_choice.strip().lower()

        if user_choice == "t":

            keyword = input("Please enter the title to search for: ")
            title_search_result = get_books_by_title(book_ibj_list, keyword)

            if len(title_search_result) == 0:
                print(f"Unfortunatelly no books were found with \"{keyword}\" in the title\n")
            else:
                print(f"There were {len(title_search_result)} books found with \"{keyword}\" in the title:\n")
                for i, book in enumerate(title_search_result, 1):
                    print(f"{i}. {book}")
                print()

            input("Press enter to return ")


        elif user_choice == "a":

            keyword = input("Please enter the author to search for: ")
            author_search_result = get_books_by_author(book_ibj_list, keyword)

            if len(author_search_result) == 0:
                print(f"Unfortunatelly no books were found with \"{keyword}\" n the autor's name\n")
            else:
                print(f"There were {len(author_search_result)} books found with \"{keyword}\" in the autor's name:\n")
                for i, book in enumerate(author_search_result, 1):
                    print(f"{i}. {book}")
                print()
            
            input("Press enter to return ")

        elif user_choice == "p":

            keyword = input("Please enter the publishing year to search for: ")
            publishing_year_search_result = get_books_by_publishing_year(book_ibj_list, keyword)
            
            if len(publishing_year_search_result) == 0:
                print(f"Unfortunatelly no books were found with \"{keyword}\" in the publishing year\n")
            else:
                print(f"There were {len(publishing_year_search_result)} books found with \"{keyword}\" in the publishing year:\n")
                for i, book in enumerate(publishing_year_search_result, 1):
                    print(f"{i}. {book}")
                print()

            input("Press enter to return ")

        elif user_choice == "g":

            keyword = input("Please enter the genre to search for: ")
            genre_search_results = get_books_by_genre(book_ibj_list, keyword)

            if len(genre_search_results) == 0:
                print(f"Unfortunatelly no books were found with \"{keyword}\" in the genre\n")
            else:
                print(f"There were {len(genre_search_results)} books found with \"{keyword}\" in the genre:\n")
                for i, book in enumerate(genre_search_results, 1):
                    print(f"{i}. {book}")

            input("Press enter to return ")

        elif user_choice == "q":

            print("Quitting search\n")
            break
        
        else:
            print(f"\"{user_choice}\" isn't a valid choice\n")