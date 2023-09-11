# Write a Python program to find given number is positive ,nigetive
# or zero.

number = int(input("please enter the number = "))

if number > 0:
    print(f"your given number = {number} is positive")
elif number < 0:
    print(f"your given number = {number} is negative ")
else:
    print(f"Your given number = {number } is zero")