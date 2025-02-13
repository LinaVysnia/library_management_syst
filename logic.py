import json
from const import *
from classes.book import Book
from classes.reader import Reader
from classes.librarian import Librarian
from datetime import datetime, timedelta
import random


#file methods
def load_books_from_file():
    """
    Takes data from the book data file turns dictionaries from the list into usable book objects and returns them as a list
        Retuns:
            A list of book objects
    """
    with open (book_data_path, "r", encoding="UTF8") as file:
    #getting raw data as a list with dict formatted book info that will need to be translated into objects
        raw_data = json.load(file) 

        #converting dict entry into a book class object
        book_obj_list = [Book(book_data["book"]["title"], 
                              book_data["book"]["author"], 
                              book_data["book"]["publishing_year"], 
                              book_data["book"]["genre"], 
                              book_data["is_borrowed"],
                              [(datetime.strptime(item[0],"%Y %m %d, %H:%M:%S"), item[1]) for item in book_data["history"]]) #why did I do this to myself
                                for book_data in raw_data]
    return book_obj_list

def save_books_to_file(book_obj_list):
    """
    Takes a list of book objects, formats it to a dictionary list and saves it to book data file by overwriting the file
        Arguments:
            A list of book objects
    """
    #formatting each book object in the list into book dictionary list
    dict_list_from_obj_list = list(map(lambda x: {
        "book" : {
            "title": x.title, 
            "author": x.author, 
            "publishing_year": x.publishing_year, 
            "genre": x.genre
            },
        "is_borrowed": x.is_borrowed,
        "history" : [(item[0].strftime("%Y %m %d, %H:%M:%S"), item[1]) for item in x.history] #this is unreadable
        }, book_obj_list))
                                       
    with open (book_data_path, "w", encoding="UTF8") as file:
        json.dump(dict_list_from_obj_list, file, indent=4)

def load_readers_from_file():
    """
    Takes data from reader data file, turns dictionaries from the list into usable reader objects and returns them as a list
        Retuns:
            A list of Reader objects
    """
    with open (reader_data_path, "r", encoding="UTF8") as file:
    #getting raw data as a list with dict formatted reader info that will need to be translated into objects
        raw_data = json.load(file) 

        reader_obj_list = [Reader(
                                reader_data["reader"]["name"], 
                                reader_data["reader"]["surname"], 
                                datetime.strptime(reader_data["reader"]["dob"],"%Y %m %d"), 
                                reader_data["reader"]["address"], 
                                reader_data["reader"]["phone_num"], 
                                reader_data["reader"]["cardID"])   
                                for reader_data in raw_data]
    return reader_obj_list

def save_readers_to_file(reader_obj_list):
    """
    Takes a list of reader objects, formats it to a dictionary list and saves it to reader data file by overwriting the file
        Arguments:
            A list of reader objects
    """
    #formatting each reader object in the list into reader dictionary list
    dict_list_from_obj_list = list(map(lambda x: {
        "reader" : {
            "name": x.name,
            "surname": x.surname,
            "dob": x.dob.strftime("%Y %m %d"),
            "address": x.address,
            "phone_num": x.phone_num,
            "cardID": x.cardID
            }
        }, reader_obj_list))
                                       
    with open (reader_data_path, "w", encoding="UTF8") as file:
        json.dump(dict_list_from_obj_list, file, indent=4)


#book methods
def print_inventory(book_obj_list):
    if len(book_obj_list) == 0:
        print("There are no books owned by the library")
    else:
        print(f"There are {len(book_obj_list)} books in the inventory:\n")
        for i, book in enumerate(book_obj_list, 1):
            print(f"{i}. {book}")
        print("\n")

def add_book(book_obj_list : list, title : str, author : str, publishing_year, genre : str, is_borrowed : bool = False, history :list = []):
    """
    Adds a book to the system by appending a new Book class object to the "book_database" list and by updating the data storage file
    Args:
        All the arguments are required
        Title, author and genre should be in a string format, if unknown enter "unknown"
    """
    new_book = Book(title, author, publishing_year, genre, is_borrowed, history)
    
    #adding the book object to library's book database
    book_obj_list.append(new_book)

    #updating the database storage file b_data.json
    save_books_to_file(book_obj_list)

    print(f"Book added: {new_book}\n")

def delete_books_older_than(book_obj_list, age):
    """
    Deletes books older than the given age
        Arguments:
            Age as an integer
    """
    is_book_too_old = lambda book : True if datetime.now().year - book.publishing_year > age else False

    #updating library's internal database
    book_obj_list = list(filter(lambda x: not is_book_too_old(x), book_obj_list))

    #updating book_data file to reflect deletion changes
    save_books_to_file(book_obj_list)

def get_available_books(book_obj_list):
    available_books = list(filter(lambda book: True if not book.is_borrowed else False, book_obj_list))
    return available_books

def get_borrowed_books(book_obj_list):
    borrowed_books = list(filter(lambda book: True if book.is_borrowed else False, book_obj_list))
    return borrowed_books

def print_borrowed_books(book_obj_list):
    unavailable_books = get_borrowed_books(book_obj_list)
    if len(unavailable_books) == 0:
        print("No the books are borrowed\n")
    else:
        print(f"There are {len(unavailable_books)} books borrowed from the library:")
        for i, book in enumerate(unavailable_books, 1):
            print(f"{i}. {book}")
            return_date = (book.history[-1][0] + timedelta(days = days_before_overdue)).strftime("%Y %m %d, %H:%M")
            print(f"it has to be returned by {return_date}\n")
        print()

def print_available_books(book_obj_list):
    available_books = get_available_books(book_obj_list)

    if len(available_books) == 0:
        print("All the books in the library are borrowed\n")
    else:
        print(f"There are {len(available_books)} books present in the library:")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. {book}")
        print()

def borrow_book(book_obj_list : list, chosen_book : Book, reader_cardID):
            """
            Takes a book objlist, a book which isn't borrowed (.is_borrowed = False) and readers card ID. 
            Sets the book status to be borrowed, adds exact datetime and attaches the reader's card ID
                Args: book obj list, a book obj and readers card ID accessed though reader_obj.cardID
            """

            #matching the chosen book to the book within the database
            matched_book : Book = book_obj_list[book_obj_list.index(chosen_book)]

            if matched_book.is_borrowed == True:
                raise Exception("The given book must not be borrowed already")
            
            matched_book.is_borrowed = True
            matched_book.history.append((datetime.now(), reader_cardID)) #appending to the history list as a touple

            save_books_to_file(book_obj_list)

def get_overdue_book_list(book_obj_list):

    def is_overdue(book : Book):

        if not book.is_borrowed:
            return False 
        #book.history[-1][0] gets the latest history entry with [-1] and the time from history item touple with [0]
        elif (datetime.now() - book.history[-1][0]).days > days_before_overdue: 
            return True
        else:
            return False

    overdue_book_list = list(filter(lambda book: is_overdue(book), book_obj_list))
    return overdue_book_list

def print_overdue_books(book_obj_list):
    overdue_book_list = get_overdue_book_list(book_obj_list)

    if len(overdue_book_list) == 0:
        print("There are no overdue books in the library\n")
    else:
        print(f"There are {len(overdue_book_list)} book(s) overdue:")
        for i, book in enumerate(overdue_book_list, 1):
            print(f"{i}. {book}.")
            print(f"Late reader's card ID is : {book.history[-1][1]}")
            print(f"Overdue by {((datetime.now() - book.history[-1][0]).days) - days_before_overdue} days\n")

def return_book(book : Book):
    book_obj_list = load_books_from_file()
    matched_book : Book = book_obj_list[book_obj_list.index(book)]

    if matched_book.is_borrowed == False:
        raise Exception("The given book must be borrowed already")
    
    matched_book.is_borrowed = False

    save_books_to_file(book_obj_list)

def get_books_by_title(book_ibj_list, keyword : str):
    keyword = keyword.lower().strip()
    books_by_title = []

    book : Book
    for book in book_ibj_list:
        title = book.title.lower().strip()
        if keyword in title:
            books_by_title.append(book)

    return books_by_title

def get_books_by_author(book_ibj_list, keyword : str):
    keyword = keyword.lower().strip()
    books_by_author = []

    book : Book
    for book in book_ibj_list:
        author = book.author.lower().strip()
        if keyword in author:
            books_by_author.append(book)

    return books_by_author

def get_books_by_publishing_year(book_ibj_list, keyword : str):
    keyword = keyword.lower().strip()
    books_by_publishing_year = []

    book : Book
    for book in book_ibj_list:
        publishing_year= str(book.publishing_year)
        if keyword in publishing_year:
            books_by_publishing_year.append(book)

    return books_by_publishing_year

def get_books_by_genre(book_ibj_list, keyword : str):
    keyword = keyword.lower().strip()
    books_by_genre = []

    book : Book
    for book in book_ibj_list:
        genre= book.genre.lower().strip()
        if keyword in genre:
            books_by_genre.append(book)

    return books_by_genre
        

#reader methods
def get_all_card_IDs(reader_obj_list):
    all_IDs = []
    for reader in reader_obj_list:
        all_IDs.append(reader.cardID)
    
    return all_IDs

def generateID (reader_obj_list, length = default_ID_length, use_num = True, use_spec_char = False):
    """
    generates an ID
    forces the use of each type of symbol by inserting them

    Args:
        must receive a list of every reader to check if the generated id is not used twice
        length must be greater than 3!
        number and special character inclusion is on by default

    Returns:
        ID of a given length
        or an error if given length is too short

    """
    if length <4:
        raise Exception("An ID must be at least 4 characters long!")
    else:
        symbols_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        symbols_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        symbols_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols_special_charatcters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", " ", ",", ".", "<", ">", "/", "?", "|", "~", "`"] #missing \

        unavailable_IDs = get_all_card_IDs(reader_obj_list)
        id_char_list = []
        character_selector = symbols_lower + symbols_upper   #the base of character selector consists of upper and lower case letters only

        if use_num:
            character_selector += symbols_numbers
        if use_spec_char:
            character_selector += symbols_special_charatcters

        for i in range(length - 4 ): # 4 is because we would force no more than 4 additional characters
            id_char_list.append(random.choice(character_selector))
        
        #forcing a lower letter to be added in the ID
        new_lower_index = random.randint(0, len(id_char_list))
        id_char_list.insert(new_lower_index, random.choice(symbols_lower))

        #forcing an upper letter to be added to the ID
        new_upper_index = random.randint(0, len(id_char_list))
        id_char_list.insert(new_upper_index, random.choice(symbols_upper))
        
        #if number inclusion is True forcing at least one number added
        if use_num:
            new_symb_index = random.randint(0, len(id_char_list))
            id_char_list.insert(new_symb_index, random.choice(symbols_numbers))
        
        #if special symbol inclusion is True forcing at least one special character added
        if use_spec_char:
            new_symb_index = random.randint(0, len(id_char_list))
            id_char_list.insert(new_symb_index, random.choice(symbols_special_charatcters))

        #generating the rest of the ID in case no numbers or special characters were requested
        while len(id_char_list) < length:
            new_symb_index = random.randint(0, len(id_char_list))
            id_char_list.append(random.choice(character_selector))

        id= "".join(id_char_list)
    
    if id in unavailable_IDs:
        return generateID() #recursion goes brrrr
    else: return id

def print_readers(reader_obj_list):
    if len(reader_obj_list) == 0:
        print("There are no registered readers at the library")
    else:
        print(f"There are {len(reader_obj_list)} readers registered at this library: ")
        for i, reader in enumerate(reader_obj_list, 1):
            print(f"{i}. {reader}")
        print()

def add_reader(reader_obj_list, name : str, surname : str, dob, address : str, phone_num : int,  cardID ):
    """
    Adds a reader to the system by appending a new Reader class object to the "reders" list and by updating the data storage file
    Args:
        All the arguments are required except cardID which is automatically generated 
    """
    new_reader= Reader(name, surname, dob, address, phone_num, cardID)
    
    #adding the Reader object to library's reader database
    reader_obj_list.append(new_reader)

    #updating the reader database storage file
    save_readers_to_file(reader_obj_list)

    print(f"Reader added: {new_reader}\n")

def get_readers_overdue_books(book_obj_list, reader : Reader):
    overdue_books = get_overdue_book_list(book_obj_list)
    readers_overdue_books = []
    for book in overdue_books:
        if book.history[-1][1] == reader.cardID:
            readers_overdue_books.append(book)

    return readers_overdue_books


#librarian methods
def load_librarians_from_file():
    """
    Takes data from librarian data file, turns dictionaries from the list into usable librarian objects and returns them as a list
        Retuns:
            A list of Librarian objects
    """
    with open (librarian_data_path, "r", encoding="UTF8") as file:
    #getting raw data as a list with dict formatted reader info that will need to be translated into objects
        raw_data = json.load(file) 

        librarian_obj_list = [Librarian( 
                                librarian_data["librarian"]["username"], 
                                librarian_data["librarian"]["password"])   
                                for librarian_data in raw_data]
    return librarian_obj_list