length_of_list = 10


def inputMethod():
    valid_input = False
    while not valid_input:
        num = input("Enter A Number for the list:")
        try:
            input_value = int(num)
            if input_value >= 0:
                return input_value
            else:
                print("Not a Valid Number! Enter a number greater than 0!")
        except:
            print("Not a Valid Number!")


def find_smallest_number(list_of_numbers):
    smallest_num = None
    for i in list_of_numbers:
        if smallest_num is None or smallest_num > i:
            smallest_num = i
    print(f'{smallest_num} is the least number')


def check_prime_number(list_of_numbers):
    for i in list_of_numbers:
        is_prime = True
        if i == 0:
            is_prime = False
        for k in range(1, i - 1):
            if (i % k == 0 and k != 1) or (i == 1):
                is_prime = False
                break
        msg = ''
        if is_prime:
            msg = 'Prime'
        else:
            msg = 'Not Prime'
        print(f'{i} is {msg}')


list_Of_Numbers = []
for m in range(1, length_of_list + 1):
    user_input = inputMethod()
    if user_input is not None:
        list_Of_Numbers.append(user_input)
print(f'The list of numbers is:{list_Of_Numbers}')
find_smallest_number(list_Of_Numbers)

check_prime_number(list_Of_Numbers)
