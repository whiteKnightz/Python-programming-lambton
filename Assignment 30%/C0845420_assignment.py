# Part-1) The simplest encryption algorithm
import math
import random


def add_seperator(msg):
    print("\n" * 5)
    print(msg)
    print("-" * 50)


def input_method(msg):
    valid_input = False
    while not valid_input:
        num = input(msg)
        try:
            input_value = int(num)
            return input_value
        except ValueError:
            print("Not a Valid Number!")


def caesar_cypher(text, cypher_key):
    encoded_string = ""
    for n in range(len(text)):
        char_val = text[n]
        char_ord = ord(char_val)
        if (65 <= char_ord <= 90) or (97 <= char_ord <= 122):
            if not char_val.isupper():
                encoded_string += chr((char_ord + cypher_key - 97) % 26 + 97)
            else:
                encoded_string += chr((char_ord + cypher_key - 65) % 26 + 65)
        else:
            encoded_string += char_val
    return encoded_string


add_seperator("Part-1) The simplest encryption algorithm")
cypher_text = input("Enter a string to encode:")
cypher_int = input_method("Enter A Number for the cypher:")
print(caesar_cypher(cypher_text, cypher_int))


# Part-2) Binary Search Algorithm Implementation in Python
def recurse_binary_search(number_list, low_index, high_index, item_val):
    if high_index < low_index:
        return -1
    else:
        mid_index = math.floor((high_index + low_index) / 2)
        if number_list[mid_index] == item_val:
            return mid_index
        elif number_list[mid_index] <= item_val:
            return recurse_binary_search(number_list, mid_index + 1, high_index, item_val)
        else:
            return recurse_binary_search(number_list, low_index, mid_index - 1, item_val)


add_seperator("Part-2) Binary Search Algorithm Implementation in Python")
list_of_num = []
for i in range(15):
    list_of_num.append(random.randint(1, 200))
list_of_num.sort()
print(f'The List is:{list_of_num}')
item = input_method("Enter A Number to search:")

index_val = recurse_binary_search(list_of_num, 0, len(list_of_num) - 1, item)

if index_val > -1:
    print(f'The index of item is:{index_val}')
else:
    print("Item not present in the list")


# Part-3) Formula Implementation
def get_factorial(int_value):
    if int_value == 0:
        return 1
    else:
        recurse_factorial = get_factorial(int_value - 1)
        return recurse_factorial * int_value


def estimate_pi():
    value = 0
    counter = 0
    first_part = (2 * math.sqrt(2) / 9801)
    can_continue = True
    while can_continue:
        numerator = get_factorial(4 * counter) * (1103 + 26390 * counter)
        denominator = (get_factorial(counter) ** 4) * (pow(396, 4 * counter))
        computed_val = (first_part * numerator) / denominator
        if computed_val < 1e-15:
            can_continue = False
        else:
            value += computed_val
        counter += 1
    return value


add_seperator("Part-3) Formula Implementation")
print(f'The computed value of PI is:{1 / estimate_pi()}')
