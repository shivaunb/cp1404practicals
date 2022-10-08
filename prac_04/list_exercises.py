"""
CP1404 Practical
Program that gets numbers from user and provides information about these numbers
Program that checks if entered username is in a list of authorised users
"""

# 1. Information about numbers entered by user
TOTAL_NUMBER = 5

numbers = []
for i in range(TOTAL_NUMBER):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2. Woefully inadequate security checker - Authorised usernames

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
