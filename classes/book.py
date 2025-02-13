class Book:
    def __init__(self, title : str, author : str, publishing_year, genre : str, is_borrowed : bool = False, history :list = []): #remember to figure out the date
        self.title = title
        self.author = author
        self.publishing_year =  publishing_year
        self.genre = genre
        self.is_borrowed = is_borrowed  #will be a bool with true if book is not present in the library
        self.history = history #should be a list of touples with the first value with a date and the second with reader's card id

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.publishing_year})" #return to this and check if  actually used this
    
    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.publishing_year})"
    
    def __eq__(self, other): #this MUST be updated every time class parameters change
        value_comparison = self.title == other.title and self.author == other.author and self.publishing_year == other.publishing_year and self.genre == other.genre and self.is_borrowed == other.is_borrowed and self.history == other.history

        return value_comparison