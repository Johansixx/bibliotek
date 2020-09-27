from Libraryclass import Lib, Book, Movie, Cd


My_library = Lib("", "")


def print_choices():
    print("""\n Välj vilken typ av media du vill lägga till i bibloteket: \n
    1.Vill du lägga till en bok?
    2.Vill du lägga till en film ?
    3.Vill du lägga till en cd-skiva ?
    4.Vill du kolla i bibloteket  ?
    0.Vill du avsluta programmet """)


print_choices()

choice = int(input("entar a number: "))


while choice != 0:
    if choice == 1:
        print("vänligen ange title, författare, sidor, pris, år")
        title = input("title: ")
        author = input("Författare: ")
        pages = input("Sidor: ")
        price = input("Pris: ")
        year = input("År: ")

        # Book(title, author, pages, year, price)
        # Book.add_book()
        My_library.add_book(title, author, pages, year, price)

    elif choice == 2:
        print("Vänligen ange title, regissör, Längd på filmen, Pris och årtal")
        title = input("title: ")
        director = input("Regissör: ")
        lenght = input("Längd: ")
        price = input("Pris: ")
        year = input("Årtal: ")

        movie = Movie(title, price)
        movie.add_movie(title, director, lenght, year, price)

    elif choice == 3:
        print("Vänligen ange title, Artist, Hur många låtar?, Längden, Pris ")
        title = input("title: ")
        artist = input("Artist: ")
        tracks = input("Låtar: ")
        lenght = input("Längd: ")
        price = input("Pris: ")

        cd = Cd(title, price).add_cd
        cd.add_cd(title, artist, tracks, lenght, price)

    elif choice == 4:
        My_library.print_books()

    elif choice == 0:
        exit()
    else:
        print("\n- Ogiltigt alternativ. Välj något mellan 1 och 4")

    print()
    print_choices()
    choice = int(input("entar a number: "))

    # 6book_ett = Lib.add_book("Bilbo", "Tolkien", 1000, 1900, 250, 1)
    # title, author, pages, year, price
