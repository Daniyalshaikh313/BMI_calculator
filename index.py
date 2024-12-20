name = input("Enter your Name: ")
weight = float(input("Enter your Weight (kg): "))
height = float(input("Enter your Height (inches): "))

# Calculate BMI using height in inches
bmi = (weight / (height ** 2)) * 703

# Check for valid BMI range
if bmi > 0:
    if bmi < 16:
        print(name + ", Your Severe Thinness")
    elif bmi >= 16 and bmi <= 16.9:
        print(name + ", Your Moderate Thinness")
    elif bmi >= 17 and bmi <= 18.4:
        print(name + ", Your Mild Thinness")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(name + ", Your Normal")
    elif bmi >= 25 and bmi <= 29.9:
        print(name + ", Your Overweight")
    elif bmi >= 30 and bmi <= 39.9:
        print(name + ", Your Obese")
    else:
        print(name + ", Your Severe Obesity")
else:
    print("Enter valid input.")

print("Thank you for visiting our page")
