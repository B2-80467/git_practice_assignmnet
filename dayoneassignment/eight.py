# Write a program that prompts the user to input number of calls and
# calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls

number_Of_Calls = int(input("please enter the number of calls = "))

if number_Of_Calls <= 100:
    ans = 200
    print(f"Your call amount is {ans}")
elif number_Of_Calls > 100 and number_Of_Calls <= 150:
    ans = 200 + (number_Of_Calls - 100)*0.60
    print(f"your call amount for {number_Of_Calls} is = {ans} ")
elif number_Of_Calls >150 and number_Of_Calls <= 200:
    ans = 200 + (50*0.60) + (number_Of_Calls - 150)*0.50
    print(f"your call amount for {number_Of_Calls} is = {ans}")
else:
    ans = 200 + (50*0.60) + (50*0.50) + (number_Of_Calls - 200)*0.40
    print(f"Your call amount for {number_Of_Calls} is = {ans}")
