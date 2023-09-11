
#5] Write a Python function to find the maximum of three numbers.


print("please enter the three numbers in the following manner ")


def samir(num1, num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"num1 {num1} is the greatest ")
    elif num2 > num3:
        print(f"num2 = {num2} is the greatest")
    else:
        print(f"num3 = {num3} is the greatest")

samir(
num1 = int(input("please enter the first number = ")),
num2 = int(input("please enter the second number = ")),
num3 = int(input("please enter the third number = "))



)

