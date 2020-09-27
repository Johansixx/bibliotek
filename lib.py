class Lib:

    pricedown = 0.9

    def __init__(self, titel, price):
        self.titel = titel
        self.price = price
        self.movie_list = []
        self.list_of_books = []
        self.cd_list = []
        self.bibblan = []

    def add_book(self, titel, author, pages, year, price):
        # new_book = input("Skriv en bok som du vill lägga in? : ")
        # new_book = Book(titel, author, int(pages), int(price), int(year))
        self.list_of_books.append(Book(titel, author, int(pages), int(year), int(price)))
    
    def print_books(self):
        if len(self.list_of_books) == 0:
            print("Listan är tom")

        for books in self.list_of_books:
            print(books)

    def add_movie(self, titel, director, lenght, year, price):
        new_movie = Movie(titel, director, lenght, price, year)
        self.movie_list.append(new_movie)

    def add_cd(self, titel, artist, tracks, lenght, price):
        new_cd = Cd(titel, artist, tracks, lenght, int(price))
        self.cd_list.append(new_cd)

    def price_down(self):
        self.price = int(self.price * self.pricedown)

    def get_titel(self):
        return self.titel

    def get_price(self):
        return self.price

    def titel_price(self):
        return "{} {}".format(self.titel, self.price)


class Book(Lib):

    price_upp = 1.08

    def __init__(self, titel, author, pages, year, price):
        super().__init__(titel, price)
        self.author = author
        self.pages = pages
        self.year = year

    def show_books(self):
        return self.titel, self.author, self.pages, self.year, self.price

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    def get_year(self):
        return self.year

    def book_value(self):
        if self.year < 1970:
            self.price = int(self.price * self.price_upp)
        elif self.year > 1970:
            pass


class Movie(Lib):
    def __init__(self, titel, director, lenght, price, year):
        super().__init__(titel, price)
        self.director = director
        self.lenght = lenght
        self.year = year

    def show_movies(self):
        return self.titel, self.director, self.lenght, self.price, self.year

    def movie_value(self):
        pass

    def get_director(self):
        return self.director

    def get_lenght(self):
        return self.lenght

    def get_year(self):
        return self.year


class Cd(Lib):
    def __init__(self, titel, artist, tracks, lenght, price):
        super().__init__(titel, price)
        self.artist = artist
        self.tracks = tracks
        self.lenght = lenght

    def show_cd(self):
        return self.titel, self.artist, self.tracks, self.lenght, self.price

    def get_artist(self):
        return self.artist

    def get_tracks(self):
        return self.tracks

    def get_lenght(self):
        return self.lenght

# def get_cd_value(self):
# for cd in self.cd_list:
# pass
