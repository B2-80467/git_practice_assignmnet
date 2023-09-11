# 1) Using for loop, write and run a Python program to find factorial from 0 to
# 10.

num = int(input("please enter your number for the factorial = "))


# factorial = 1;
#
# while( num >= 1):
#     """here i am going to write the logic for the factorial """
#
#     factorial = factorial * num;
#
#     num -= 1;
#
#
# print(f"your factorial is = {factorial}")

factorial = 1;
for val in range(num,0,-1):
    # print(f" my values are {val}")

    factorial = factorial * val

print(f"your factorial value is = {factorial} ")