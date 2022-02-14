#PASSWORD GENERATOR

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '@', '$', '%', '&', '*', '+', '(', ')']
print("WELCOME TO PYPASSWORD GENERATOR.")
letters_wanted = int(input("How many letters would you like in your password: "))
numbers_wanted = int(input("How many digits would you like in your password: "))
characters_wanted = int(input("How many symbols would you like in your password: "))

password_str = ''
for n in range(1, letters_wanted+1):
    password_str += random.choice(letters)

for n in range(1, numbers_wanted+1):
    password_str += random.choice(numbers)

for n in range(1, characters_wanted+1):
    password_str += random.choice(symbols)

password_list = list(password_str)
random.shuffle(password_list)
print(f"Your password could be: {''.join(password_list)}.")