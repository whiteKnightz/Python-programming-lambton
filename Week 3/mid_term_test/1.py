list_of_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']


def inputMethod():
    valid_input = False
    while not valid_input:
        num = input("Enter A Number for the list:")
        try:
            input_value = int(num)
            if input_value > 0:
                return input_value
            else:
                print("Not a Valid Number! Enter a number greater than 0!")
        except:
            print("Not a Valid Number!")


def pyramid(number_value):
    char_list_len = len(list_of_char)
    for i in range(0, number_value):
        index_num = i
        if i >= char_list_len:
            index_num = i % char_list_len
        print(list_of_char[index_num]*(i+1))


number  = inputMethod()
if number  is not None:
    pyramid(number )
