class Lib:

    pricedown = 0.9

    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.movie_list = []
        self.list_of_books = []
        self.cd_list = []
        self.current_value = 0

    def add_book(self):
        my_list = []
        my_list.append(self.title + self.price + self.author + self.pages + self.year)
        print(my_list)

    def print_books(self):
        if len(self.list_of_books) == 0:
            print("Listan är tom")

        for books in self.list_of_books:
            print(books.show_books())

    def add_movie(self, title, director, length, year, price):
        self.movie_list.append(Movie(title, director, int(length), int(year), int(price)))

    def print_movies(self):
        if len(self.movie_list) == 0:
            print("listan är tom")

        for movies in self.movie_list:
            print(movies.show_movies())

    def add_cd(self, title, artist, tracks, length, price):
        self.cd_list.append(Cd(title, artist, int(tracks), int(length), int(price)))

    def print_cds(self):
        if len(self.cd_list) == 0:
            print("listan är tom")

        for cds in self.cd_list:
            print(cds.show_cds())

    def price_value(price, year):
        value = price
        if year != 0:
            for year in range(1, year+1):
                value = value * 0.9
        return value

    def title_price(self):
        return "{} {}".format(self.title, self.price)


class Book(Lib):

    def __init__(self, title, price, author, pages, year):
        super().__init__(title, price)
        self.author = author
        self.pages = pages
        self.year = year

    '''def add_book(self):
        my_list = []
        my_list = (self.title, self.author, self.pages, self.year, self.price)
        self.list_of_books.append(my_list)'''

    def show_books(self):
        return f"{self.title}, {self.author}, {self.pages}, {self.year}, {self.price}"

    def book_value(self):
        if self.year < 1970:
            self.price = int(self.price * self.price_upp)
        elif self.year > 1970:
            pass


class Movie(Lib):
    def __init__(self, title, director, length, price, year):
        # super().__init__(title, price)
        self.director = director
        self.length = length
        self.year = year

    def show_movies(self):
        return f"{self.title},{self.director},{self.length},{self.price},{self.year}"


class Cd(Lib):
    def __init__(self, title, artist, tracks, length, price):
        self.artist = artist
        self.tracks = tracks
        self.length = length

    def show_cd(self):
        return f"{self.title}, {self.artist}, {self.tracks}, {self.length}, {self.price}"
