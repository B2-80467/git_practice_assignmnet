# The marks obtained by a student in 3 different subjects are input by the user. Your
# program should calculate the average of subjects and display the grade. The student
# gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

#stpe 1 = take marks obtained by the user

math  = int(input("please enter your math marks = "))
sci = int(input("please enter your sci marks = "))
phy = int(input("please enter your phy marks = "))

Avg = (math + sci + phy)/3

if Avg <= 100 and Avg >= 90:
    print(f"Your Avg is {Avg} and your gread is A")
elif Avg <= 89 and Avg >= 80:
    print(f"your Avg is {Avg} and your gread is B")
elif Avg <= 79 and Avg >= 70:
    print(f"Your Avg is {Avg} and your gread is C")
elif Avg <= 69 and Avg >= 60:
    printf(f"")


    