# Write a Python Program find an area of a rectangle and perimeter
# of the rectangle

# rectangle l * b
# perimeter of rect 2(l+b)


length = int(input("please enter the length of the rectangle = "))

breadth = int(input("please enter the breadth of the rectangle = "))


area_Of_Rect = length * breadth

perimeter_Of_Rect = 2*(length + breadth)

print(f"Area of rectangle is {area_Of_Rect}")
print(f"Perimeter_Of_rectangle is {perimeter_Of_Rect}")
