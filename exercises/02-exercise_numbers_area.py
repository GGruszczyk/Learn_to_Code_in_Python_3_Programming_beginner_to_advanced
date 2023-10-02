#Data types: Numbers
#modulo can be used to determine odd and even numbers
#round(num, decimalPlaces)
#import math (brings in math module of functions)
#math.factorial(5) 5*4*3*2*1 math.floor rounds up math.floor rounds
#a remainder in modulus will always return "1"
# https://docs.python.org/3/library/math.html

# IDLE practice
# num1 = 5
# num2 = 3
# type(num1)
# <class 'int'>
# res = num1 / num2
# type(res)
# <class 'float'>
# res
# 1.6666666666666667
# round(res, 2)
# 1.67
# num1 = 102931.60
# num1 = 5
# num1 + num2
# 8
# num1 - num2
# 2
# num1 * num2
# 15
# num1 / num2
# 1.6666666666666667
# num1 % num2
# 2
# num1 ** num2
# 125
# (2 + 2)/3
# 1.3333333333333333
# ((2 + 2)/3)/4
# 0.3333333333333333


#Calculate the area and circumference of a circle. Ask the user for the radius.

#my attempt
#import math

#radius = input("Give me the radius and I'll calculate the area and circumference of a circle!")
#area = math.pi(radius **2)

#circumference = 2 * (math.pi(radius))

#print("Area:", area)
#print("Circumference:", circumference)

#questions: difference between using "," and "+"; 

# multi line comment with """

import math

print("This program will calculate the area and circumference of a circle given its radius")
radius = float(input("Type the radius of the circle: "))
area = math.pi * (radius **2) #parentheses for heirarchy of operations
circumference = 2 * math.pi * radius

print("The area of the circle is", round(area, 2), "The circumference is:", round(circumference, 2))

# https://www.gigacalculator.com/calculators/circumference-of-circle-calculator.php