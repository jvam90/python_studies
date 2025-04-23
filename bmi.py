height = input("What is your height (inches): ")
weight = input("What is your weight (pounds): ")

height_value = float(height)
weight_value = float(weight)

bmi = (weight_value * 703) / (height_value ** 2)

if bmi < 16.0:
    print("Severely underweight")
elif bmi >= 16.0 and bmi < 18.4:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal")
elif bmi >= 25.0 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30.0 and bmi < 34.9:
    print("Moderately obese")
elif bmi >= 35.0 and bmi < 39.9:
    print("Severely obese")
else:
    print("Morbidly obese")