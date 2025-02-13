import os
import json
from const import book_data_path, reader_data_path, librarian_data_path

def create_book_data():
    """
    Creates dummy book data iif no such file exists
    """
    if os.path.isfile(book_data_path):
        print(f"{book_data_path} file found. Dummy data creation is skipped\n")
    else: 
        print(f"{book_data_path} file not found. Initialising dummy data\n")

        #these are the 10 dummy books to fill the book database
        books = [
            {"title": "To Kill a Mockingbird", 
             "author": "Harper Lee", 
             "publishing_year": 1960, 
             "genre": "Fiction"},

            {"title": "1984", 
             "author": "George Orwell", 
             "publishing_year": 1949, 
             "genre": "Dystopian"},

            {"title": "Pride and Prejudice", 
             "author": "Jane Austen", 
             "publishing_year": 1813, 
             "genre": "Romance"},

            {"title": "The Great Gatsby", 
             "author": "F. Scott Fitzgerald", 
             "publishing_year": 1925, 
             "genre": "Fiction"},

            {"title": "Moby Dick", 
             "author": "Herman Melville", 
             "publishing_year": 1851, 
             "genre": "Adventure"},

            {"title": "War and Peace", 
             "author": "Leo Tolstoy", 
             "publishing_year": 1869, 
             "genre": "Historical Fiction"},

            {"title": "The Hobbit", 
             "author": "J.R.R. Tolkien", 
             "publishing_year": 1937, 
             "genre": "Fantasy"},

            {"title": "Brave New World", 
             "author": "Aldous Huxley", 
             "publishing_year": 1932, 
             "genre": "Dystopian"},

            {"title": "The Catcher in the Rye", 
             "author": "J.D. Salinger", 
             "publishing_year": 1951, 
             "genre": "Fiction"},

            {"title": "The Alchemist", 
             "author": "Paulo Coelho", 
             "publishing_year": 1988, 
             "genre": "Philosophical Fiction"}
        ]

        #initialising a dictionary from the list
        books_to_database = list(map(lambda x: {"book" : x, "is_borrowed" : False, "history" : []}, books))

        with open (book_data_path, "w", encoding="UTF8") as file:
            json.dump(books_to_database, file, indent=4)

def create_reader_data():
    """
    Creates dummy reader data if no such file exists
    """ 
    if os.path.isfile(reader_data_path):
        print(f"{reader_data_path} file found. Dummy data creation is skipped\n")
    else: 
        print(f"{reader_data_path} file not found. Initialising dummy data\n")

        #these are the 5 dummy readers to fill the reader database
        readers = [
            {
                "name": "Frodo",
                "surname": "Baggins",
                "dob": "1995 09 22",
                "address": "12 Bag End, Hobbiton, Shire",
                "phone_num": "555-123-4567",
                "cardID": "FR0D0B4GG1"
            },
            {
                "name": "Arwen",
                "surname": "Undmiel",
                "dob": "1988 06 15",
                "address": "15 Evenstar Lane, Rivendell",
                "phone_num": "555-987-6543",
                "cardID": "4RW3NUND0M"
            },
            {
                "name": "Geralt",
                "surname": "of Rivia",
                "dob": "1990 04 10",
                "address": "3 Kaer Morhen Drive, Rivia",
                "phone_num": "555-345-6789",
                "cardID": "G3R4LT0FRV"
            },
            {
                "name": "Lyra",
                "surname": "Silvertongue",
                "dob": "2000 12 07",
                "address": "22 Jordan College Way, Oxford",
                "phone_num": "555-567-8901",
                "cardID": "LYR4S1LVRT"
            },
            {
                "name": "Jon",
                "surname": "Snow",
                "dob": "1994 01 16",
                "address": "Castle Black, The Wall, North",
                "phone_num": "555-789-0123",
                "cardID": "J0NSN0WC4S"
            }
        ]

        #initialising a dictionary from the list
        readers_to_database = list(map(lambda x: {"reader" : x}, readers))
        
        with open (reader_data_path, "w", encoding="UTF8") as file:
            json.dump(readers_to_database, file, indent=4)

def create_librarian_data():
    """
    Creates dummy librarian data if no such file exists
    """
    if os.path.isfile(librarian_data_path):
        print(f"{librarian_data_path} file found. Dummy data creation is skipped\n")
    else: 
        print(f"{librarian_data_path} file not found. Initialising dummy data\n")

        #a couple of librarians to fill the book database
        librarians = [
            {"username": "admin", 
             "password": "Linai 10"},

            {"username": "Lina", 
             "password": "Man 10"}
        ]

        #initialising a dictionary from the list
        librarians_to_database = list(map(lambda x: {"librarian" : x}, librarians))
        
        with open (librarian_data_path, "w", encoding="UTF8") as file:
            json.dump(librarians_to_database, file, indent=4)


def create_dummy_data():
   create_book_data()
   create_reader_data()
   create_librarian_data()