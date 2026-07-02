print("Hello, this is age calculator. Input your birthday and I will compute your age based on the inputted birthyear.")

name = input("name? ")
Byear = int(input("birth year? "))

age = 2026 - Byear
Hyear = Byear + 100

print(f"Hello, {name}")
print(f"your age is approximately {age}")
print(f"you will be 100 in year {Hyear}")