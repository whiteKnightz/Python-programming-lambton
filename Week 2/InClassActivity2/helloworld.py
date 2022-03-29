"""
This is a sample Python script containing print_info function.
It takes four parameter input as name, description, program, courses
It prints those value in a formatted way

"""


def print_info(name, description, program, courses):
    print("\n\n" +
          "Name: %s \n Description: %s \n Program: %s \n Courses: %s" % (name, description, program, courses),
          end=".\n\n")


name_value = "Abhishek Satyal"
description_value = "I am from Biratnagar, Nepal. I worked as full-stack Java developer. " \
                    "I also serve as technical team lead"
program_value = "Cloud Computing for Big Data"
courses_value = "Python Programming, Operating Systems Foundations, Big Data Fundamentals - Data Storage Networking" +\
          "Database Design, Networking Foundations, Virtualization"

print_info(name_value, description_value, program_value, courses_value)
