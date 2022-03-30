import re

"""
1) Write a Python function that takes a string and calculates the length of a string and returns it. 
    Print the returned value.

2) Write a Python function that takes a string and counts the number of characters (character frequency) in a string. 
    For example, if we send 'google.com' to the function, it should return a dictionary like this 
    {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

3) Create a string of your choice and apply a minimum of 8 of following methods to it and print the result.
    https://docs.python.org/3.8/library/string.html

4) Write a Python function that converts temperatures from Fahrenheit to Celsius.

"""


def add_seperator(msg):
    print("\n" * 5)
    print(msg)
    print("-" * 50)


def first_question():
    add_seperator('1. Length of the string')
    input_data = input("Please enter a string to test:")
    return len(input_data)


len_of_string = first_question()
print(f'Length of string is: {len_of_string}')


def second_question():
    add_seperator('2. Dictionary for word count')
    input_st = input("Please enter a string to test?").lower()
    list_of_chars = []
    for i in input_st:
        if list_of_chars.count(i) < 1:
            list_of_chars.append(i)
    result_dictionary = {}
    for i in list_of_chars:
        result_dictionary[i] = input_st.count(i)
    print(f'The final dictionary is: {result_dictionary}')


second_question()


def third_question():
    add_seperator('3. 8 valid methods of string')
    data_string = "This man is the greatest footballer of all time"
    print(f'The data string is:\t\t\"{data_string}\"')
    print(f'The result of capitalisation is:\t\t\"{data_string.capitalize()}\"')
    print(f'The result of casefold is:\t\t\"{data_string.casefold()}\"')
    print(f'The result of count for \"the\" is:\t\t{data_string.count("the")}')
    print(f'The result of string ending with \"the\" is:\t\t{data_string.endswith("the")}')
    print(f'The result of centering string with 80 is:{data_string.center(80)}')
    print(f'The result of encoding with \"ascii\" is:\t\t{data_string.encode(encoding="ascii")}')
    print(f'The result of finding \"all\" is:\t\t{data_string.find("all")}')
    data_string = "This man, {player}, is the greatest footballer of all time"
    print(f'The un-formatted string is:\t\t{data_string}')
    print(f'The result of formatting of the string is:\t\t{data_string.format(player="Ronaldo Lima")}')


third_question()


def get_valid_temp():
    valid_temp = False
    temp_data = None
    while not valid_temp:
        try:
            input_data = input("Please enter a temperature in Fahrenheit:")
            temp_data = float(input_data)
            valid_temp = True
        except ValueError:
            print("Invalid temperature! Please re-try!")
    return temp_data


def forth_question():
    add_seperator('4. Convert temperatures from Fahrenheit to Celsius')
    temp_f = get_valid_temp()
    temp_c = ((temp_f - 32) * 5) / 9
    print(f'The temperature in Celsius is {temp_c}')


forth_question()
