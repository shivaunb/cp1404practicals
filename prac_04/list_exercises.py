"""
CP1404 Practical
Program that gets numbers from user and provides information about these numbers
"""
TOTAL_NUMBER = 5

numbers = []
for i in range(TOTAL_NUMBER):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")

