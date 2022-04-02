import datetime
import math
from dateutil.relativedelta import relativedelta


def add_seperator(msg):
    print("\n" * 5)
    print(msg)
    print("-" * 50)


def first_question():
    add_seperator("1. Use the datetime module to write a program that gets the current date and prints the day of "
                  "the week.")
    datetime_now = datetime.datetime.now()
    print(f'Today is: {datetime_now.strftime("%A")}')


first_question()


def input_method(msg):
    valid_input = False
    while not valid_input:
        date_value = input(msg)
        try:
            return datetime.datetime.strptime(date_value, '%d/%m/%y')
        except ValueError:
            print("Not a Valid DOB format!")


def second_question():
    add_seperator("2. Write a program that takes a birthday of user as input and prints the user’s age and the "
                  "number of days, hours, minutes and seconds until their next birthday.")
    datetime_dob = input_method("Add valid date of birth in DD/MM/YY format(Example:22/07/91):\n")
    datetime_now = datetime.datetime.now()
    datetime_difference = datetime_now - datetime_dob
    date_string = "{date}/{month}/{year}"
    datetime_bd_this_year = datetime.datetime.strptime(
        date_string.format(date=datetime_dob.strftime("%d"), month=datetime_dob.strftime("%m"),
                           year=datetime_now.strftime("%y")), '%d/%m/%y')
    datetime_bd_next_year = datetime_bd_this_year + relativedelta(years=1)
    datetime_next_bd = datetime_bd_this_year if (datetime_bd_this_year >= datetime_now) else datetime_bd_next_year
    print(
        f'You are: {math.floor((datetime_difference.days + datetime_difference.seconds / 86400) / 365.2425)} years old')
    print(f'Next birthday is in {datetime_next_bd-datetime_now}')


second_question()


def third_question():
    add_seperator("3. Write a program that takes birthday of a person and calculates the total number of seconds "
                  "they have been living in epoch time")
    datetime_dob = input_method("Add valid date of birth in DD/MM/YY format(Example:22/07/91):\n")
    datetime_diff = datetime.datetime.now()-datetime_dob
    print(f'You have lived for {datetime_diff.total_seconds()} seconds in epoch time.')


third_question()


def forth_question():
    add_seperator("4. Write a Python program to print the date for yesterday, today, and tomorrow.")
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    print('Yesterday : ', yesterday)
    print('Today : ', today)
    print('Tomorrow : ', tomorrow)


forth_question()
