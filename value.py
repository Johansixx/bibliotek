import json

def books_value(content):
    print("Books:")
    for item in content:
        purchase_year = item["purchase_year"]
        price = int(item["price"])
        yearnow = 2019
        age = yearnow - int(purchase_year)
        print(str("Age = ") + str(age))
        if age == 0:
            value = price
        elif age > 50:
            age = age - 50
            value = price * 1.08 * age
        else:
            value = price * 0.9**age
        print(str("Tittel: ") + item["title"])
        print(str("Författare: ") + item["author"])
        print(str("Published: ") + str(purchase_year))
        print(str("Ålder: ") + str(age))
        print(str("Current price: ") + str(value))
        print(str("\n"))
    return value


def cd_value(content):
    print("CDs:")
    for item in content:
        title = item["title"]
        artist = item["artist"]
        price = item["price"]
        tracks = item["tracks"]
        length = item["length"]
        value = item["price"]
        print(str("Tittel: ") + item["title"])
        print(str("Artist: ") + item["artist"])
        print(str("tracks: ") + str(tracks))
        print(str("length: ") + str(length))
        print(str("Current price: ") + str(price))
        print(str("\n"))
        return item


def movie_value(content):
    print("Movies:")
    for item in content:
        title = item["title"]
        director = item["director"]
        purchase_year = item["purchase_year"]
        price = int(item["price"])
        condition = item["condition"]
        if condition == 10:
            price = price
        else:
            condition = condition / 10
            price = price * condition
        print(str("Tittel: ") + item["title"])
        print(str("pris: ") + str(price))
        print(str("director: ") + str(item["director"]))
        print(str("purchase_year: ") + str(item["purchase_year"]))
        print(str("condition: ") + str(item["condition"]))
        print(str("\n"))
        return item
