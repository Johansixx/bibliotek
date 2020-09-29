import value


class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Media):

    def __init__(self, title, author, pages, purchase_year, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages
        self.purchase_year = purchase_year 
        self.current_value = 0

    def set_library_value(self):
        self.current_value = value.book_value(self.price, self.purchase_year)

    def show_books(self):
        return f"""Book: Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Purchase year: {self.purchase_year}, Price:{self.price}"""


class Movie(Media):
    def __init__(self, title, director, length, purchase_year, price, condition):
        super().__init__(title, price)
        self.director = director
        self.length = length
        self.purchase_year = purchase_year
        self.condition = condition

    def show_movies(self):
        return f"""Movie: Title: {self.title}, Director: {self.director}, length: {self.length}, Price: {self.price}, purchase year: {self.purchase_year}"""
    
    def set_library_value(self):
        self.current_value = value.movie_value(self.price, self.purchase_year, self.condition)


class Cd(Media):
    def __init__(self, title, artist, tracks, length, price):
        super().__init__(title, price)
        self.artist = artist
        self.tracks = tracks
        self.length = length

    def show_cd(self):
        return f"""CD: Title: {self.title}, Artist: {self.artist},Tracks: {self.tracks}, length: {self.length}, Price: {self.price}"""

    def set_library_value(self, amount):
        self.current_value = value.cd_value(self.price, amount)
