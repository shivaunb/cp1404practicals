MINIMUM = 8
password = input("Enter Password: ")
password_length = len(password)
while password_length < MINIMUM:
    print("Invalid Password")
    password = input("Enter Password: ")
    password_length = len(password)
for i in range(password_length):
    print("*", end="")