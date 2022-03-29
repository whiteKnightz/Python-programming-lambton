def add_seperator(msg):
    print("\n" * 5)
    print(msg)
    print("-" * 50)


add_seperator("4-1. Pizza")


# 4-1. Pizza
def print_pizza(*pizzas):
    for pizza in pizzas:
        print(f'I love {pizza} pizza.')
    print(f'I love pizza. ')


pizza_list = ["Margareta", "Pepperoni", "Chicken Kebab"]
print_pizza(*pizza_list)

add_seperator("4-2. Animal")


# 4-2. Animal
def print_wild_cats(*wild_cats):
    for wild_cat in wild_cats:
        print(f'{wild_cat} are great hunters.')
    print(f'All of these animal roar and belongs to the cat family.')


wild_cats = ["Lion", "Tiger", "Leopard", "Panther"]
print_wild_cats(*wild_cats)

add_seperator("4-3. Counting to 20")

# 4-3. Counting to 20
for i in range(1, 21):
    print(i)

add_seperator("4-4. One Million")

# 4-4. One Million
million_range = range(1, 1000001)
for i in million_range:
    print(i)

add_seperator("4-5. Summing a Million")

# 4-5. Summing a Million
print(f'Min of list is {min(million_range)}')
print(f'Max of list is {max(million_range)}')
print(f'Sum of list is {sum(million_range)}')

add_seperator("4-6. Odd Numbers")

# 4-6. Odd Numbers
odd_number = range(1, 20, 2)
for i in odd_number:
    print(i)

add_seperator("4-13. Buffet")


# 4-13. Buffet
def print_menu(foods):
    print(f'Food in the menu:')
    for index, food in enumerate(foods):
        print(f'{index + 1}. {food}')


foods_tuple = ("Pizza", "Carbonara", "Croissant", "Knafeh", "Shawarma")
print_menu(foods_tuple)
try:
    foods_tuple[1] = "Momo"
except:
    print("Tulip modification not allowed")
foods_tuple = ("Lamb Kebab", "Carbonara", "Croissant", "Black Forest", "Shawarma")
print("\nMenu was changed\n\n")
print_menu(foods_tuple)

add_seperator("8-3. T-Shirt")


# 8-3. T-Shirt
def make_shirt(size, message):
    print(f'The size of shirt is: {size} \nIt has following message: {message}')


make_shirt("XL", "Peace was never an option")
make_shirt(message="Peace was never an option", size="XL")

add_seperator("8-4. Large Shirts")


# 8-4. Large Shirts
def make_shirt(size="Large", message="I love Python"):
    print(f'The size of shirt is: {size} \nIt has following message: {message}')


make_shirt("Large")
make_shirt("Medium")
make_shirt("Small", "Peace was never an option")

add_seperator("8-5. Cities")


# 8-5. Cities
def describe_city(city, country="Spain"):
    print(f'{city} is in {country}')


describe_city(city="Barcelona")
describe_city(city="Madrid")
describe_city(city="Paris", country="France")

add_seperator("8-6. City Names")


# 8-6. City Names
def city_country(city, country):
    return city + "," + country


print(city_country("Barcelona", "Spain"))
print(city_country("Madrid", "Spain"))
print(city_country("Paris", "France"))

add_seperator("8-7. Album")


# 8-7. Album
def make_album(artist, album, no_of_songs=None):
    dictionary = {"Artist's Name": artist, "Album's Title": album}
    if no_of_songs is not None:
        dictionary["no_of_songs"] = no_of_songs
    return dictionary


print(make_album("Linkin Park", "Meteora"))
print(make_album("Eurielle", "Arcadia"))
print(make_album("Infected Mushroom", "Head of NASA and the 2 Amish Boys"))
print(make_album("Eluveitie", "Origins", 20))

add_seperator("8-8. User Albums")

# 8-8. User Albums
get_input = True
while get_input:
    artist = input("Enter a artist name:")
    album = input("Enter a album name:")
    print(make_album(artist=artist, album=album))
    decision = input("Want to continue with more[Y/n]: ")
    if decision.upper().strip() == "N":
        get_input = False
