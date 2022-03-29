# 2-1 Simple Message

message_1 = 'Hello! Welcome to the class'
print(f'The message is:{message_1}')





print('\n\n\n')
# 2-2 Simple Messages

print(f'The message is:{message_1}')
message_1 = 'Hello! Welcome to the class, student'
print(f'New message is:{message_1}')





print('\n\n\n')
# 2-3 Personal Message

person_name = input('Enter your name:')
print(f'Hello {person_name}, would you like to lear some Phyton today?')






print('\n\n\n')
# 2-4 Name Cases

print(f'Name in lowercase:{person_name.lower()}')
print(f'Name in uppercase:{person_name.upper()}')
print(f'Name in titlecase:{person_name.title()}')






print('\n\n\n')
# 2-5 Famous Quote

print('Johan Cruyff once said, "Quality without results is pointless. Results without quality is boring."')





print('\n\n\n')
# 2-6 Famous Quote 2
famous_person = 'Johan Cruyff'
message = 'Quality without results is pointless. Results without quality is boring.'
print(f'{famous_person} once said, "{message}"')




print('\n\n\n')
# 2-7 Stripping Names
person_name = '\t  Johan Cruyff   \n '
print(f'Raw persson name: {person_name}')
print(f'Persson name with lstrip: {person_name.lstrip()}')
print(f'Persson name with rstrip: {person_name.rstrip()}')
print(f'Persson name with strip: {person_name.strip()}')




print('\n\n\n')
# 2-8 Number Eight
print(4+4)
print(10-2)
print(1*8)
print(64//8)



print('\n\n\n')
# 2-9 Favourite Number
favourite_number = 7
message = 'My favourite number is:'+str(favourite_number)
print(message)