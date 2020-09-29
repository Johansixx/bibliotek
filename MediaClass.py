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


class Movie(Media):
    def __init__(self, title, director, length, purchase_year, price, condition):
        super().__init__(title, price)
        self.director = director
        self.length = length
        self.purchase_year = purchase_year
        self.condition = condition


class Cd(Media):
    def __init__(self, title, artist, tracks, length, price):
        super().__init__(title, price)
        self.artist = artist
        self.tracks = tracks
        self.length = length
