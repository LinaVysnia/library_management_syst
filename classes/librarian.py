class Librarian:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, input):
        if self.__password == input:
            return True
        else:
            return False