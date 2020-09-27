from lib import Lib, Book, Movie, Cd


My_library = Lib("titel", "price")


def print_choices():
    print("""\n Välj vilken typ av media du vill lägga till i bibloteket: \n
    1. Lägg till en bok?
    2. Lägg till en film ?
    3. lägg till en cd-skiva ?
    4. Kolla i bibloteket  ?
    0. Avsluta programmet """)


print_choices()

choice = int(input("entar a number: "))


while choice != 0:
    if choice == 1:
        print("vänligen ange titel, författare, sidor, pris, året boken kom ut?")
        titel = input("Titel: ")
        author = input("Författare: ")
        pages = input("Sidor: ")
        price = input("Pris: ")
        year = input("År: ")

        My_library.add_book(titel, author, pages, year, price)

    elif choice == 2:
        print("Vänligen ange Titel, regissör, Längd på filmen, Pris och årtal")
        titel = input("Titel: ")
        director = input("Regissör: ")
        lenght = input("Längd: ")
        price = input("Pris: ")
        year = input("Årtal: ")

        movie = Movie(titel, price)
        movie.add_movie(titel, director, lenght, year, price)

    elif choice == 3:
        print("Vänligen ange Titel, Artist, Hur många låtar?, Längden, Pris ")
        titel = input("Titel: ")
        artist = input("Artist: ")
        tracks = input("Låtar: ")
        lenght = input("Längd: ")
        price = input("Pris: ")

        cd = Cd(titel, price).add_cd
        cd.add_cd(titel, artist, tracks, lenght, price)

    elif choice == 4:
        My_library.print_books()

    elif choice == 0:
        exit()
    else:
        print("\n- Ogiltigt alternativ. Välj något mellan 1 och 4")

    print()
    print_choices()
    choice = int(input("entar a number: "))

    #6book_ett = Lib.add_book("Bilbo", "Tolkien", 1000, 1900, 250, 1)
    # titel, author, pages, year, price
