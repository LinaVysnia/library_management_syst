from abc import ABC, abstractmethod

class StateMachineRunner:
    def run():
        state = StartState()
        while state:
            state = state.next()
        print('finished running state machine')

class State(ABC):
    @abstractmethod
    def next():
      print('running and returning next state')
      return StopState()

class StartState(State):
   def next():
      print('starting')
      return BookMenuState()

class StopState(State):
   def next():
      print('stopping')
      return None
    
class BookMenuState(State):
    def next():
        print("*" * 80)
        print("Main menu\n")
        print("Please enter the menu item number to select it")
        print(
        """
        1. View library's book inventory
        2. View overdue books
        3. View borrowed books
        4. View books available for booking
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
            return LibraryBookInventoryViewState()
        return BookMenuState()
    
class LibraryBookInventoryViewState(State):
    def next():
        print("*" * 80)
        print("Viewing library's book inventory\n")
        print_book_inventory()
        input("Press enter to return ")
        return BookMenuState()
    
