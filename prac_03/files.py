"""
CP1404 - Practical
Experience with different ways to read files
"""

# Question 1
user_name = input("Enter your name: ").title()
out_file = open("name.txt", "w")
print(user_name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
user_name = in_file.read().strip()
in_file.close()
print(f"Your name is {user_name}")

# Question 3
in_file = open("numbers.txt", "r")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
print(f"{number_one} + {number_two} = {number_one + number_two}")

# Question 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"Your total is {total}")
