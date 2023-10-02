# comparison operators > < == != >= <=
# num1 = 8
# num2 = 4
# num1 > num2 #True
# num1 != num2 #False

# num1 = float(input("Type the first number: "))
# num2 = float(input("Type the second number: "))

# booleans inside conditional statements
# if num1 > num2:
#     print(num1, "is greater than", num2)
# elif num1 == num2:
#     print(num1, "is equal to", num2)
# else:
#     print(num1, "is less than", num2)

# Exercise: Create a program and store your age in a variable. Then ask the user for his age and print whether:
userAge = int(input("What's your age? "))
myAge = 34

if userAge > myAge:
    print("You're older than me! I'm 34.")
elif userAge == myAge:
    print("No way. I'm 34 also!")
else:
    print("You're younger than me! I'm 34.")