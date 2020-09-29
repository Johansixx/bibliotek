
from MediaClass import Book, Movie, Cd

import json

class Lib:
    def __init__(self):
        self.movie_list = []
        self.list_of_books = []
        self.cd_list = []

    def write_json(self, data, filename='Libraryfile.json'): 
        with open(filename, 'w') as f: 
            json.dump(data, f, indent=4) 

    def add_book(self, title, author, pages, purchase_year, price):

        book = {
		"title": title,
		"author": author,
        "purchase_year": purchase_year,
		"pages": pages,
        "price": price,
        }
        

        # dumps används för att formatera book rätt. Alltså till en string +  att den 
        # gör så att json loads förstår formatet
        book = json.dumps(book)
        # loads gör så att python fattar att det är ett json-objekt och inte en string bara
        book = json.loads(book)
        booksfile = open("Libraryfile.json")
        booksjson = json.load(booksfile)
        booksfile.close()
        books = booksjson["books"]
        books.append(book)
        self.write_json(booksjson)

    def add_cd(self, title, artist, tracks, length, price):

        cd = {
		"title": title,
		"artist": artist,
        "tracks": tracks,
		"length": length,
        "price": price,
        }

        cd = json.dumps(cd)
        cd = json.loads(cd)
        cdsfile = open("Libraryfile.json")
        cdsjson = json.load(cdsfile)
        cdsfile.close()
        cds = cdsjson["cds"]
        cds.append(cd)
        self.write_json(cdsjson)

        # self.cd_list.append(Cd(title, artist, int(tracks), int(length), float(price)))

    def add_movie(self, title, director, length, purchase_year, price, condition):

        movie = {
		"title": title,
		"director": director,
		"length": length,
        "purchase_year": purchase_year,
        "price": price,
        "condition": condition,
        }

        movie = json.dumps(movie)
        movie = json.loads(movie)
        moviesfile = open("Libraryfile.json")
        moviesjson = json.load(moviesfile)
        moviesfile.close()
        movies = moviesjson["movies"]
        movies.append(movie)
        self.write_json(moviesjson)
        #self.movie_list.append(Movie(title, director, int(length), int(purchase_year), float(price), int(condition)))

    def print_books(self):
        if len(self.list_of_books) == 0:
            print("Book list is empty")
        for books in self.list_of_books:
            print(books.show_books())

    def print_movies(self):
        if len(self.movie_list) == 0:
            print("Movie list is empty")
        for movies in self.movie_list:
            print(movies.show_movies())

    def print_cds(self):
        if len(self.cd_list) == 0:
            print("CD list is empty")
        for cds in self.cd_list:
            print(cds.show_cd())
