from logic import get_all_card_IDs, load_readers_from_file
from classes.reader import Reader
from UI.readers_main_UI import run_readers_main_UI

def run_reader_login_UI():
    all_readers = load_readers_from_file()
    card_IDs = get_all_card_IDs(all_readers)

    print("Helper for available IDs: ", card_IDs)
    while True:
        
        user_input = input("Please enter your reader's card ID or \"l\" to return to the login page: ").strip()

        if user_input == "":
            print("Please enter something")
        
        elif user_input.lower() == "l":
            break

        elif user_input in card_IDs:
            matched_reader : Reader = None
            for reader in all_readers:
                if reader.cardID == user_input:
                    matched_reader : Reader = reader
                    break
                
            run_readers_main_UI(matched_reader)
            break
        
        else:
            print(f"\"{user_input}\" isn't a valid option, please make another entry")
        
