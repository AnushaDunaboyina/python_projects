# Create a Password Generator

import random
import string

print("Welcome to the PyPassword Generator")

letters = int(input("How many letters would you like in your password? "))

symbols= int(input("How many symbols would you like in your password? "))

numbers = int(input("How many numbers would you like in your password? "))

# In string form
# password = ""

# for n in range(1, letters + 1):
#     letter = random.choice(string.ascii_letters)
#     password += letter

# for n in range(1, symbols + 1):
#     symbol = random.choice(string.punctuation)
#     password += symbol

# for n in range(1, numbers + 1):
#     number = random.randint(0, 9)
#     password += str(number)

# print(f"Password: {password}")

# In List form

password_list = []

for n in range(1, letters +1):
    password_list.append(random.choice(string.ascii_letters))

for n in range(1, symbols + 1):
    password_list.append(random.choice(string.punctuation))

for n in range(1, numbers + 1):
    password_list.append(str((random.randint(0, 9))))

#random.shuffle(password_list)

password_chars = ''.join(password_list)
print(f"Password is: {password_chars}")