class Reader:
    def __init__(self, name : str, surname : str, dob, address : str, phone_num : int,  cardID :str):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.phone_num = phone_num
        self.cardID = cardID

    def __str__(self):
        return f"{self.name} {self.surname} ({self.cardID})"