class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.media_list = []


class Book(Media):

    def __init__(self, title, price, author, pages, year):
        super().__init__(title, price)
        self.author = author
        self.pages = pages
        self.year = year

    def add_book(self):
        my_list = []
        my_list.append(self.title + self.price + self.author + self.pages + self.year)
        print(my_list)


test = Book('test', '2', '2', '2', '2')
test.add_book()























''''def show_books(self):
        return f"{self.titel}, {self.author}, {self.pages}, {self.year}, {self.price}"

class Movies(media):
    def __init__(self, titel, director, lenght, price, year):
        self.director = director
        self.lenght = lenght
        self.year = year

    def show_movies(self):
        return f"{self.titel}, {self.director}, {self.lenght}, {self.price}, {self.year}"

class CD(media):
    def __init__(self, titel, artist, tracks, lenght, price):
        self.artist = artist
        self.tracks = tracks
        self.lenght = lenght

 def show_cd(self):
        return f"{self.titel}, {self.artist}, {self.tracks}, {self.lenght}, {self.price}"
'''
