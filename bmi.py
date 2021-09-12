def BMI(height, weight):
    bmi = weight/(height ** 2)
    return bmi

# driver code
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in lbs: "))



# calling bmi function
bmi = BMI(height, weight)

# conditions to find out BMI category
if (bmi < 18,5):
    print("You're underweight")

elif (bmi >= 18.5 and bmi < 24.9):
    print("Desirable")

elif (bmi >= 24.9 and bmi < 30):
    print("Overweight")

elif (bmi >= 30):
    print("Suffering from obesity")
