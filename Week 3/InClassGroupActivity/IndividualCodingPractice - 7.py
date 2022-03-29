import re

"""
1. Create a Program to check whether the given input (Student ID) is in a Specific Format(ABC123)

    Step 1: Take Input from the user ( Any String)
    
    Step 2: Check the length of the String if the length is 6.
    
    Step 3:  Logic


2. Create a Program to check whether a particular string starts with "The".
"""


def add_seperator(msg):
    print("\n" * 5)
    print(msg)
    print("-" * 50)


def first_question():
    add_seperator('1. Match the pattern similar to \'ABC123\'')
    input_id = input("Please enter a student ID?")
    result = re.findall("[A-za-z]{3}[0-9]{3}", input_id)
    if len(result) == 1:
        print(f'{input_id} is a valid Student ID!')
    else:
        print(f'{input_id} is an invalid Student ID!')


first_question()


def second_question():
    add_seperator('2. Match if the string starts with \'The\'')
    input_st = input("Please enter a string to test:")
    result = re.findall("^The.*$", input_st)
    if result:
        print(f'\'{input_st}\' starts with \'The\'!')
    else:
        print(f'\'{input_st}\' doesn\'t starts with \'The\'!')


second_question()

