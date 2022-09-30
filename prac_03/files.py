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


