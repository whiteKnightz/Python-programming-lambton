import random

"""
1. create a list using random module print the random numbers from 1-10 and add unique numbers to your list.

2. print the maximum number from list without using max function

3. print min number without using min()

4. sort the list without using sort()
"""


def add_seperator(msg):
    print("\n" * 5)
    print(msg)
    print("-" * 50)


def test_condition(msg, condition):
    print(msg)
    print(condition)


def find_max(number_list):
    maximum = None
    for i in number_list:
        if maximum is None or maximum < i:
            maximum = i
    return maximum


def find_min(number_list):
    maximum = None
    for i in number_list:
        if maximum is None or maximum > i:
            maximum = i
    return maximum


def sort_list(number_list):
    number_list_len = len(number_list)
    for m in range(number_list_len):
        for n in range(0, number_list_len - m - 1):
            if number_list[n] > number_list[n + 1]:
                low_num = number_list[n + 1]
                number_list[n + 1] = number_list[n]
                number_list[n] = low_num
    return number_list


list_of_number = random.sample([*range(1, 11)], 10)
# for i in range(1, 10):
#     list_of_number.append(random.sample(1, 10))
print(f'The list is: {list_of_number}')
print(f'Max in the list is: {find_max(list_of_number)}')
print(f'Min in the list is: {find_min(list_of_number)}')
print(f'Sorted list is: {sort_list(list_of_number)}')


def first_question():
    add_seperator("5-1. Conditional Test")
    singer = "Eminem"
    test_condition('Is the singer == Metallica? I predict False', singer == "Metallica")
    test_condition('Is the singer == Eminem? I predict True', singer == "Eminem")
    test_condition('Is the singer != Eminem? I predict False', singer != "Eminem")
    selected_num = 77
    test_condition('Is the selected_num == 77? I predict True', selected_num == 77)
    test_condition('Is the selected_num < 79? I predict True', selected_num < 79)
    test_condition('Is the selected_num <= 76? I predict False', selected_num <= 76)
    test_condition('Is the selected_num >= 76? I predict True', selected_num >= 76)
    test_condition('Is the selected_num > 8? I predict True', selected_num > 8)
    test_condition('Is length of list_of_number == 8? I predict False', len(list_of_number) == 8)
    test_condition('Is length of list_of_number > 11? I predict False', len(list_of_number) > 11)


first_question()


def second_question(number_list):
    add_seperator("5-2. More Conditional Test")
    fav_game = "Witcher 3"
    test_condition('Is fav_game != Far Cry 5? I predict True', fav_game != "Far Cry 5")
    test_condition('Is fav_game != Witcher 3? I predict False', fav_game == "Far Cry 5")
    test_condition('Is fav_game != witcher 3? I predict True', fav_game != "Witcher 3".lower())
    selected_num = 420
    test_condition('Is the selected_num == 420? I predict True', selected_num == 420)
    test_condition('Is the selected_num < 500? I predict True', selected_num < 500)
    test_condition('Is the selected_num <= 400? I predict False', selected_num <= 400)
    test_condition('Is the selected_num >= 330? I predict True', selected_num >= 330)
    test_condition('Is the selected_num > 81? I predict True', selected_num > 81)
    test_condition('Is (1>2) or (8*9-6==64)? I predict True', (1 > 2) or (8 * 9 - 6 == 66))
    test_condition('Is (1>2) and (8*9-6==64)? I predict False', (1 > 2) and (8 * 9 - 6 == 64))
    test_condition('Does number_list has item 1? I predict True', number_list.count(1) > 0)
    try:
        print("Does number_list not have item 23? I predict True")
        number_list.index(23)
    except ValueError:
        print("Don't have in the list!!")


second_question(list_of_number)


def check_alien_color_is_green(color):
    if color.lower() == "green":
        print("Congrats! You earned 5 points")


def third_question():
    add_seperator("5-3. Alien Color #1")
    alien_color = "green"
    check_alien_color_is_green(alien_color)
    alien_color = "yellow"
    check_alien_color_is_green(alien_color)


third_question()


def check_alien_color(color):
    if color.lower() == "green":
        print("Congrats! You earned 5 points")
    elif color.lower() != "green":
        print("Congrats! You earned 10 points")


def fourth_question():
    add_seperator("5-4. Alien Color #2")
    alien_color = "green"
    check_alien_color(alien_color)
    alien_color = "yellow"
    check_alien_color(alien_color)


fourth_question()


def check_all_alien_color(color):
    if color.lower() == "green":
        print("Congrats! You earned 5 points")
    elif color.lower() == "yellow":
        print("Congrats! You earned 10 points")
    elif color.lower() == "red":
        print("Congrats! You earned 15 points")


def fifth_question():
    add_seperator("5-5. Alien Color #3")
    alien_color = "green"
    check_all_alien_color(alien_color)
    alien_color = "yellow"
    check_all_alien_color(alien_color)
    alien_color = "red"
    check_all_alien_color(alien_color)


fifth_question()


def determine_stage_of_person(age_of_person):
    if age_of_person < 2:
        print("The person is a baby")
    elif 2 <= age_of_person < 4:
        print("The person is a toddler")
    elif 4 <= age_of_person < 13:
        print("The person is a kid")
    elif 13 <= age_of_person < 20:
        print("The person is a teenager")
    elif 20 <= age_of_person < 65:
        print("The person is a adult")
    elif 65 <= age_of_person:
        print("The person is a elder")


def sixth_question():
    add_seperator("5-6. Stages of Life")
    is_valid_input = False
    while not is_valid_input:
        age_value = input("Enter an age for the person!!")
        try:
            age = float(age_value)
            is_valid_input = True
            determine_stage_of_person(age)
        except ValueError:
            print("Give a valid input please!!")
            is_valid_input = False


sixth_question()


def is_favorite_fruit(fruit_name):
    favorite_fruit = ["Apple", "Mango", "Cranberry"]
    if favorite_fruit.count(fruit_name) > 0:
        print(f'You really like {fruit_name}')


def seventh_question():
    add_seperator("5-7. Favorite Fruit")
    fruits = ["Pineapple", "Grapes", "Cranberry", "Banana", "Apple"]
    for fruit in fruits:
        is_favorite_fruit(fruit)


seventh_question()


def greet_users(user_list):
    if user_list is None or len(user_list) < 1:
        print("We need to find some user")
    for user_name in user_list:
        if user_name.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f'Hello {user_name}, thank you for logging in again.')


def get_valid_username():
    user = None
    valid_input = False
    while not valid_input:
        data = input("Add a username:")
        if len(data) > 0:
            valid_input = True
            user = data
        else:
            print("Enter a valid username")
    return user


def eighth_question():
    add_seperator("5-8. Hello Admin")
    users = ["admin"]
    for i in enumerate(range(1, 5)):
        users.append(get_valid_username())
    greet_users(users)


eighth_question()


def ninth_question():
    add_seperator("5-9. No Users")
    users = []
    greet_users(users)
    for i in enumerate(range(1, 3)):
        users.append(get_valid_username())
    greet_users(users)


ninth_question()


def tenth_question():
    add_seperator("5-10. Checking Usernames")
    current_users = ["Avi", "Krishh", "Bipul", "Chattra", "Arbind"]
    new_users = ["krishh", "Bish", "chattra", "Kiran", "Janvhee"]
    for user in new_users:
        if [m.lower() for m in current_users].count(user.lower()) > 0:
            print(f'{user} will need to enter new user name')
        else:
            print(f'Username is available: {user}')


tenth_question()


def eleventh_question():
    add_seperator("5-11. Ordinal Number")
    numbers = range(1, 10)
    for n in numbers:
        if n == 1:
            print(f'{n}st')
        elif n == 2:
            print(f'{n}nd')
        elif n == 3:
            print(f'{n}rd')
        else:
            print(f'{n}th')


eleventh_question()
