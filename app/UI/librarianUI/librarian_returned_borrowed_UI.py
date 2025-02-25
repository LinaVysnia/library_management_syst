from app.services.book_service import return_book, get_borrowed_books
from app.core.const import days_before_overdue
from datetime import timedelta

def run_return_book_librarian_UI():
    print("*" * 80)
    print("Returning borrowed books\n")
    borrowed_books = get_borrowed_books()

    if not borrowed_books :
        print("There aren't any borrowed books at the moment\n")
        return
        
    print(f"There are currently {len(borrowed_books)} books borrowed:\n")
    print(f"{'Title':^30}{'Author':^20}{'Publishing year:'}")
    for i, book, history in enumerate(borrowed_books, 1):
        print(f"{i}. {book}")
        return_date = (book.history[-1][0] + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
        print(f"it has to be returned by {return_date}\n")
        print()

    while True:
        book_index = input(f"Which book (1 to {len(borrowed_books)}) would you like to return? Enter 'q' to quit.")
        book_index =  book_index.strip().lower()

        if book_index == "q" or book_index == "quit":
            print("Quitting book return.")
            return
        
        try:
            int(book_index) >= 1 and int(book_index) <= len(borrowed_books)
            book_index = int(book_index) - 1
            chosen_book_with_history = borrowed_books[book_index]
            break

        except:
            print(f"Your choice isn't valid. Please enter a number between 1 and {len(borrowed_books)}")
            continue

    return_book(chosen_book_with_history)

    print(f"You have successfully returned {chosen_book_with_history}")

input("Press enter to return ")