"""
CP1404 - Practical
Experience with different ways to read files
"""

# Question 1
user_name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(user_name, file=out_file)
out_file.close()

