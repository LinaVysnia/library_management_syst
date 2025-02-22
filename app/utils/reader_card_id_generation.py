from app.core.const import default_ID_length
from random import random

from utils.card_id_duplication_check import check_if_id_duplicated

def generateID (length = default_ID_length, use_num = True, use_spec_char = False):
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
    
    id_duplicated = check_if_id_duplicated(id)

    if id_duplicated:
        return generateID()
    else: return id