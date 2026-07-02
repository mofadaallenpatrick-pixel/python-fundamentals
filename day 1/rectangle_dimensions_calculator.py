print("Rectangle calculator. this will calculate the area and diameter of the reactangle if you input the width and height.")

width = float(input("input the width: "))
height = float(input("input the height: "))

area = (width * height)
perimeter = 2 * (width + height)
diagonal = (width**2 + height**2)**0.5

print(f"The area of the rectangle is, {round(area, 2)}")
print(f"The Perimeter of the rectangle is, {round(perimeter, 2)}")
print(f"The Digonal of the rectangle is, {round(diagonal, 2)}")