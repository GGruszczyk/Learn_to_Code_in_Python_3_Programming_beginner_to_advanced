# Create a program to calculate the BMI of a person. Ask the user for his height in meter and weight in kg
# BMI = weight / (height * weight)
# BMI = (weight /(height * height)) * 703

# other than forgetting to round and replacing "input" with "print" I got the solution on my own
print("This program caluclates your BMI using your weight (lbs) and height (in)")
userWeight = float(input("Please enter your weight (lbs): "))
userHeight = float(input("Please enter your height (in): "))

BMIconversion = (userWeight / (userHeight**2)) * 703

print("BMI: ", round(BMIconversion, 2))

if BMIconversion <= 18.5:
    print("According to the BMI scale you're Underweight")
elif BMIconversion >= 18.5 or BMIconversion == 24.9:
    print("According to the BMI scale you're Normal Weight")
elif BMIconversion < 24.9 or BMIconversion <= 29.9:
    print("According to the BMI scale you're Overweight")
elif BMIconversion >= 30:
    print("According to the BMI scale you're Obese")

