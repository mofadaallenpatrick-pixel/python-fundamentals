print("This is a BMI Calculator. input your weight and height to determine if you are underweight, normal, Overweight, or obese.")

height = float(input("input your Height in meter(m): "))
weight = float(input("input your weight in kilograms(kg): "))

bmi = weight / (height**2)

if bmi < 18.5:
    print(f"You are underweight. This is your score: {round(bmi, 2)}")

elif 18.5 <= bmi <25:
    print(f"You are normal weight. This is your score: {round(bmi, 2)}")

elif 25 <= bmi <30:
    print(f"You are overweight. This is your score: {round(bmi, 2)}")

elif bmi >= 30:
    print(f"You are obese. This is your score: {round(bmi, 2)}")
