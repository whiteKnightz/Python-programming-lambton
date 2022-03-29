"""
By group 2

Abhishek Satyal
Vineet Kumar Pattam
Juan Posso
Sai Priya Akkaladevi
"""
from copy import copy


def firstQuestion():
    # List
    list_value = ["Abhishek", "Juan", "Sai Priya", "Vineet"]
    print(f'Original list: {list_value}')
    list_value.append("Simrandeep")
    print(f'After append: {list_value}')
    print(f'Count of Sai Priya: {list_value.count("Sai Priya")}')
    print(f'Index of Juan: {list_value.index("Juan")}')
    list_value.insert(2, "Arun")
    print(f'After insert on 2: {list_value}')
    list_value.pop()
    print(f'After pop: {list_value}')
    list_value.remove("Abhishek")
    print(f'After remove `Abhishek`: {list_value}')
    list_value.reverse()
    print(f'Reverse the list:{list_value}')
    list_value.sort()
    print(f'Sort the list:{list_value}')
    list_value.clear()
    print(f'List after Clear:{list_value}')

    # Tuple
    # Not available methods: append, clear, insert, pop, remove, reverse, and sort
    tuple_value = ("Abhishek", "Juan", "Sai Priya", "Vineet")
    print(f'Original tuple: {tuple_value}')
    print(f'Count of Sai Priya: {tuple_value.count("Sai Priya")}')
    print(f'Index of Juan: {tuple_value.index("Juan")}')

    # set
    # Not available methods: append, count, index, insert, reverse, and sort
    set_value = {32, "Juan", "Sai Priya", "Vineet"}
    print(f'Original set: {set_value}')
    set_value.pop()
    print(f'After pop: {set_value}')
    set_value.remove("Juan")
    print(f'After remove `Abhishek`: {set_value}')
    print(f'Sort the set:{set_value}')
    set_value.clear()
    print(f'set after Clear:{set_value}')

    # dictionary
    # Not available methods: append, count, index, insert, remove, reverse, and sort
    dictionary_value = {"Laptop ": "Hp", "OS": "Windows", "Year": 2021, "Model": "Pavilion 14", "Price": 999.99}
    print(f'Original dictionary: {dictionary_value}')
    dictionary_value["Data"] = "kjasncdlaksnlda"
    print(f'After append: {dictionary_value}')
    dictionary_value.pop("Data")
    print(f'After pop: {dictionary_value}')
    dictionary_value.clear()
    print(f'dictionary after Clear:{dictionary_value}')


def secondQuestion():
    dictionary_data = {1: ["Data 1", 1.0, 22], "Key 2": ["Data 2", 2.0, 25], 3.0: "Value Data"}
    print(f'Original dictionary:{dictionary_data}')
    dictionary_data[77] = ["Data 3", 9.0, 27]
    print(f'Dictionary after key-value added:{dictionary_data}')


def thirdQuestion():
    fruit = ("apple", "banana", "cherry")
    print(f'Type of:{type(fruit)}')
    list_value = list(fruit)
    print(f'Type of:{type(list_value)}')


def fourthQuestion():
    list_1 = [1, 4, "Juan"]
    list_2 = ["Sai Priya", "Vineet", 78.0]
    list_3 = list_1 + list_2
    print(f'First list:{list_1}')
    print(f'Second list:{list_2}')
    print(f'Combined list:{list_3}')

    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    tuple3 = tuple1 + tuple2
    print(f'First tuple:{tuple1}')
    print(f'Second tuple:{tuple2}')
    print(f'Type of final tuple:{type(tuple3)}')
    print(f'Combined tuple:{tuple3}')

    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    set3 = set.union(set1, set2)
    print(f'First set:{set1}')
    print(f'Second set:{set2}')
    print(f'Combined set:{set3}')

    dictionary1 = {"Laptop ": "Hp", "Price": 999.99}
    dictionary2 = {"OS": "Windows", "Year": 2021, "Model": "Pavilion 14"}
    dictionary3 = copy(dictionary1)
    dictionary3.update(dictionary2)
    print(f'First dictionary:{dictionary1}')
    print(f'Second dictionary:{dictionary2}')
    print(f'Combined dictionary:{dictionary3}')


firstQuestion()
secondQuestion()
thirdQuestion()
fourthQuestion()

