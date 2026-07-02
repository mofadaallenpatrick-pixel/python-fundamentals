print("This is a Number Classifier. input any number and the system will know if it is negative, positive, or zero and determine if it is even or odd. ")

number = float(input("Input any number: "))

if number < 0 and number % 2 == 0:
    print("your number is negative. and even.")

elif number < 0 and number % 2 == 1:
    print("your number is negative. and odd.")

elif number > 0 and number % 2 == 0:
    print("your number is positive and even.")

elif number > 0 and number % 2 == 1:
    print("your number is positive and odd.")

elif number == 0:
    print("your number is zero.")

else:
    print("your number is not Applicable.")