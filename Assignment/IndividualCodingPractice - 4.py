from copy import copy


def print_invitation(custom_msg=""):
    print(f'Number of people invited:{len(list_of_guest)}')
    for guest in list_of_guest:
        print(f'You are{custom_msg} invited to the Dinner on 28th of Feburary 2022 {guest}')


def replace_guest():
    global list_of_guest
    for guest in list_of_guest_not_able:
        print(f'{guest} is not available to join the dinner.')
        list_of_guest.remove(guest)
    list_of_guest = list_of_guest + new_guest_list


def append_more_guest():
    global new_guest_list
    global list_of_guest
    new_guest_list.append("Ram")
    list_of_guest.insert(0, "Ram")
    new_guest_list.append("Vishal")
    list_of_guest.insert(len(list_of_guest), "Vishal")
    new_guest_list.append("Mayank")
    list_of_guest.append("Mayank")


def shrink_guest_list():
    global list_of_guest
    global list_of_guest_not_able
    while len(list_of_guest) > 2:
        name = list_of_guest.pop()
        list_of_guest_not_able.append(name)
        print_apology_message(name)


def print_apology_message(name):
    print(f'Sorry {name} but due to some difficulty in the reservation I cannot invite you for the planned dinner.')


# 3-4 Guest list
list_of_guest = ["Rita", "Arbind", "Chattra", "Kiran", "Dipesh", "Dilip"]
print_invitation()

print("\n\n\n\n")
# 3-5 Change Guest list
list_of_guest_not_able = ["Dipesh", "Dilip"]
new_guest_list = ["Ishaan", "Simran"]
replace_guest()
print_invitation()

print("\n\n\n\n")
# 3-6 More guest
print("I was able to secure a bigger table.\n\n")
append_more_guest()
print_invitation()

print("\n\n\n\n")
# 3-7 Shrink guest list
shrink_guest_list()
print("\n\n\n\n")
print_invitation(" still")
del list_of_guest[1]
del list_of_guest[0]
print(f'List of guest:{list_of_guest}')


def print_original_list_of_place(message="Original list of places"):
    print(f'{message}:{list_of_places}')


print("\n\n\n\n")
# 3-8 Seeing the world
list_of_places = ["Barcelona", "Reykjavík", "Paris", "Tokyo", "Istanbul"]
print_original_list_of_place()
print(f'Sorted list of places:{sorted(list_of_places)}')
print_original_list_of_place()
print(f'Reverse sorted list of places:{sorted(list_of_places, reverse=True)}')
print_original_list_of_place()
list_of_places.reverse()
print_original_list_of_place("Original list of places after reverse")
list_of_places.reverse()
print_original_list_of_place("Original list of places after reversing the reversed")
list_of_places.sort()
print_original_list_of_place("Sorted original list of places")
list_of_places.sort(reverse=True)
print_original_list_of_place("Reverse sorted original list of places")

print("\n\n\n\n")
# 3-10 Every function of list
list_value = ["Dipesh", "Dilip", "Hari"]
print(f'Original list: {list_value}')
list_value.append("Arbind")
print(f'After append: {list_value}')
print(f'Count of Dipesh: {list_value.count("Dipesh")}')
print(f'Index of Dilip: {list_value.index("Dilip")}')
list_value.insert(1, "Kiran")
print(f'After insert on 1: {list_value}')
list_value.pop()
print(f'After pop: {list_value}')
list_value.remove("Dipesh")
print(f'After remove `Dipesh`: {list_value}')
list_value.reverse()
print(f'Reverse the list:{list_value}')
list_value.sort()
print(f'Sort the list:{list_value}')
list_value.clear()
print(f'List after Clear:{list_value}')

print("\n\n\n\n")
# Dictionary practice
dictionary_data = {"Database Design": "Linchen Wang", "Virtualization": "Linchen Wang",
                   "Python Programming": "Simrandeep Kaur",
                   "Operating Systems Foundations": "Mike Aleshams",
                   "Big Data Fundamentals - Data Storage Networking": "Kritika Buttan",
                   "Networking Foundations": "Albert Danison"}
print(f'Original dictionary:{dictionary_data}')
dictionary_data["Big Data Fundamentals - Data Storage Networking"] = "Linchen Wang"
print(f'Dictionary after key-value added:{dictionary_data}')
