from LibClass import Lib
import json
from value import cd_value, books_value, movie_value
My_library = Lib()


def print_choices():
    print("""\n Välj vilken typ av media du vill lägga till i bibloteket: \n
1 .Vill du lägga till en bok?
2. Vill du lägga till en film ?
3. Vill du lägga till en cd-skiva ?
4. Vill du kolla i bibloteket  ?
0. Vill du avsluta programmet """)


print_choices()

choice = int(input("\n Gör ett val: "))


while choice != 0:
    if choice == 1:
        print("vänligen ange title, författare, sidor, Inköpsår, år")
        title = input("Titel: ")
        author = input("Författare: ")
        pages = int(input("Sidor: "))
        price = float(input("Pris: "))
        purchase_year = int(input("Inköpsår: "))

        My_library.add_book(title, author, pages, purchase_year, price)


    elif choice == 2:
        print("""Vänligen ange Titel, regissör, Längd på filmen, Pris,Inköpsår och skick""")
        title = input("Titel: ")
        director = input("Regissör: ")
        length = int(input("Längd: "))
        price = float(input("Pris: "))
        purchase_year = int(input("Inköpsår: "))
        condition = int(input("""skala 1-10 då 1 är lägst, hur sliten är filmen?: """))

        My_library.add_movie(title, director, length, purchase_year, price, condition)

    elif choice == 3:
        print("Vänligen ange title, Artist, Hur många låtar?, Längden, Pris ")
        title = input("Titel: ")
        artist = input("Artist: ")
        tracks = input("Låtar: ")
        length = input("Längd: ")
        price = input("Pris: ")
        My_library.add_cd(title, artist, tracks, length, price)

    elif choice == 4:

        libraryfile = open("Libraryfile.json")
        libraryjson = json.load(libraryfile)

        books = libraryjson["books"]
        print(str("Books = ") + str(books))
        books_value(books)

        cds = libraryjson["cds"]
        print(str("CD's = ") + str(cds))
        cd_value(cds)

        movies = libraryjson["movies"]
        print(str("Movies = ") + str(movies))
        movie_value(movies)

    elif choice == 0:
        exit()

    else:
        print("\n- Ogiltigt alternativ. Välj något mellan 1 och 4")

    print()

    print_choices()

    choice = int(input("Gör ett val: "))
