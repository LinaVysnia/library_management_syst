from datetime import datetime, date
from logic import add_reader, generateID, get_all_card_IDs

def run_add_reader_UI(reader_obj_list : list):

    continue_adding_readers = True

    while continue_adding_readers:
        print("*" * 80)
        print("Registering a new reader at thew library\n")

        def print_reader_registration_progress (name = "?", surname = "?", dob = "?", address = "?", phone_num = "?", cardID = "?"):
            print(
    f"""
New reader information:
Name - {name}
Surname - {surname}
Date of birth - {dob}
Address - {address}
Phone number - {phone_num}
Reader's card ID - {cardID}
    """)
        
        print("Please enter the required information")
        print_reader_registration_progress()

        while True:
            name = input("Enter reader's name: " ).strip()
            if name != "":
                break
            else:
                print("Please enter something")
        
        print_reader_registration_progress(name)

        while True:
            surname = input("Enter reader's surname: " ).strip()
            if surname != "":
                break
            else:
                print("Please enter something")
        
        print_reader_registration_progress(name, surname)

        while True:
            dob = input("Enter the reader's date of birth as YYYY MM DD: " ).strip()
            if dob == "":
                print("Please enter something")

            else:
                try:
                    dob = datetime.strptime(dob, '%Y %m %d').date()            
                    if dob > date.today():
                        print("Unfortunatelly, library doesn't except readers from the future yet\n")

                    elif dob.year < 1800:
                        print("The library only accepts living people. You must have entered the birth date wrong\n")
                    
                    else:
                        break
                except:
                    print(f"\"{dob}\" isn't a valid date")
        
        print_reader_registration_progress(name, surname, dob)
        
        while True:
            address = input("Enter reader's address: " ).strip()
            if address != "":
                break
            else:
                print("Please enter something")

        print_reader_registration_progress(name, surname, dob, address)

        while True:
            phone_num = input("Enter reader's phone number: " ).strip()
            if phone_num != "":
                break
            else:
                print("Please enter something")

        print_reader_registration_progress(name, surname, dob, address, phone_num)

        card_ID = generateID(reader_obj_list)

        continue_choosing_ID_option = True
        while continue_choosing_ID_option:
            print("Would you like to assign a specified ID to this reader? \"no\" would auto-generate an ID. (y/n) ")
            print(
    """
    Enter \"y\" for yes
    Enter \"n\" for no
    """)
            user_choice = input("Your choice: ").lower().strip()
            if user_choice == "y" or user_choice == "yes":
                while True:
                    card_ID = input("Please specify the reader card's ID: " ).strip()
                    if card_ID == "":
                        print("Please enter something")
                    elif card_ID in get_all_card_IDs(reader_obj_list):
                        print("This card ID is already assigned to somebody else")
                    else:
                        continue_choosing_ID_option = False
                        break

            elif user_choice == "n" or user_choice == "no":
                print(f"user card's auto-generated ID is: {card_ID}")
                continue_choosing_ID_option = False
            else:
                print(f"{user_choice} isn't a valid choice")

        while True:
            print("*" * 80)
            print_reader_registration_progress(name, surname, dob, address, phone_num, card_ID)
            print("Would you like to add this reader to the library's database?")
            print(
    """
Enter \"y\" for yes
Enter \"r\" to restart
Enter \"q\" to quit adding the new reader
    """)
            user_choice = input("Your choice: ").lower().strip()

            if user_choice == "y" or user_choice == "yes":

                add_reader(reader_obj_list, name, surname, dob, address, phone_num, card_ID)

                continue_adding_readers = False
                break
            elif user_choice == "r" or user_choice == "restart":
                print("Restarting\n")
                break
            elif user_choice == "q" or user_choice == "quit":
                print("Quitting adding reader")
                continue_adding_readers = False
                break
            else:
                print(f"{user_choice} isn't a valid choice\n")
    input("Press enter to return ")