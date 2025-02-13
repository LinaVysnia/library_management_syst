from logic import return_book, get_borrowed_books, load_books_from_file
from const import days_before_overdue
from datetime import timedelta

def run_return_book_librarian_UI():
    print("*" * 80)
    print("Returning borrowed books\n")
    all_books = load_books_from_file()
    all_borrowed_books = get_borrowed_books(all_books)

    if len(all_borrowed_books) == 0:
        print("There aren't any borrowed books yet\n")
    
    else:
        
        print(f"There are currently {len(all_borrowed_books)} books borrowed:\n")
        for i, book in enumerate(all_borrowed_books, 1):
            print(f"{i}. {book}")
            return_date = (book.history[-1][0] + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
            print(f"it has to be returned by {return_date}\n")
            print()

        while True:
            book_index = input(f"Which book (1 to {len(all_borrowed_books)}) would you like to return?: ")

            try:
                if int(book_index) >= 1 and int(book_index) <= len(all_borrowed_books):
                    book_index = int(book_index) - 1
                    chosen_book = all_borrowed_books[book_index]
                    break
                else:
                    raise Exception
            except:
                print(f"Your choice isn't valid. Please enter a number between 1 and {len(all_borrowed_books)}")

        return_book(chosen_book)

        print(f"You have successfully returned {chosen_book}")

    input("Press enter to return ")