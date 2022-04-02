"""
    Coding Practice 8
    Abhishek Satyal - C0845420
    Juan Posso - C0810093
    Suryansh Gupta - C0855842
"""


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
            if input_value >= 1:
                return input_value
            else:
                print("Not a Valid Number!")
        except ValueError:
            print("Not a Valid Number!")


def first_question():
    add_seperator("Question 1: Print First 10 natural numbers using while loop")
    for i in range(10):
        print(i)


first_question()


def second_question():
    add_seperator("2: Print the following pattern")
    for i in range(1, 6):
        st_to_print = ""
        for n in range(1, i):
            st_to_print += str(n) + " "
        print(st_to_print)


second_question()


def third_question():
    add_seperator("Question 3: Accept number from user and calculate the sum of all number between 1 and given number.")
    num = input_method("Enter a valid grater than 0:")
    sum_int = 0
    for i in range(num + 1):
        sum_int += i
    print(f'The sum is:{sum_int}')


third_question()


def forth_question():
    add_seperator("Question 4: Print multiplication table of given number.")
    num = input_method("Enter a valid grater than 0:")
    for i in range(1, 11):
        print(f'{num} X {i}\t= {i * num}')


forth_question()


def fifth_question(num_list):
    add_seperator("Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find "
                  "number greater than 150 stop the loop iteration.")
    for i in num_list:
        if i > 150:
            break
        else:
            if i % 5 == 0:
                print(i)


list_of_num = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
fifth_question(list_of_num)


def sixth_question():
    add_seperator("Question 6: Given a number count the total number of digits in a number")
    number = input_method("Enter a number ")

    print("Total number of digits : ", len(str(abs(number))))


sixth_question()


def seventh_question():
    add_seperator("Question 7: Print the following pattern using for loop.")
    range_list = list(range(1, 6))
    range_list.reverse()
    for i in range_list:
        data_str = ""
        for n in range(1, i + 1):
            data_str = str(n) + " " + data_str
        print(data_str)


seventh_question()


def eighth_question(original_list):
    add_seperator("Question 8: Reverse the following list using for loop.")
    reversed_list = list()
    for item in original_list:
        reversed_list.insert(0, item)
    print(reversed_list)


list_of_number = [10, 20, 30, 40, 50]
eighth_question(list_of_number)


def ninth_question():
    add_seperator("9: Display a message “Done” after successful execution of for loop.")
    for i in range(0, 2):
        print(i)

    else:
        print("Done")


ninth_question()


def tenth_question():
    add_seperator("Question 10: Display Fibonacci series up to 10 terms.")
    n_terms = input_method("How many terms? ")
    n1, n2 = 0, 1
    count = 0

    # check if the number is valid
    if n_terms <= 0:
        print("Please enter a positive integer")
    # if there is only one
    elif n_terms == 1:
        print("Fibonacci sequence upto", n_terms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < n_terms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


tenth_question()


def eleventh_question():
    add_seperator("Question 11: Write a loop to find the factorial of any number.")
    num = input_method("enter a number: ")

    fac = 1

    for i in range(1, num + 1):
        fac = fac * i

    print("factorial of ", num, " is ", fac)


eleventh_question()


def twelfth_question():
    add_seperator("Question 12: Python program to display all the prime numbers within a range.")
    start = input_method("Enter the starting range:")
    end = input_method("Enter the end range: ")

    print("Prime numbers in the range", start, "to", end)

    for i in range(start, end + 1):
        flag = 0
        for j in range(2, i):
            if (i % j == 0):
                flag = 1
                break

        if (flag == 0):
            print(i, end=' ')


twelfth_question()
