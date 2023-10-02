# Question for Python Meetup: How can I clean up my comments?
# **Issue: not moving on to the second test**
# making sure data is valid and within range

# create variable before input, set to false
dataValid = False
# start a loop (while == false)
while dataValid == False:
    grade1 = input("Type the grade of the first test: ")
    # check to see if valid number
    try:
        grade1 = float(grade1)
    # catch with prompt for user
    except:
        print(
            "Invalid input. Only numbers are accepted and decimals separated with a dot."
        )
        # in  order to make conversion and prevent crash
        continue
    # create conditional for parameters
    if grade1 < 0 or grade1 > 10:
        # add print statement  for validation
        print("Grades must be between 0 and 10")
        # jumps out of the loop and starts again
        continue
    # else statement concludes valid input ending loop
    else:
        dataValid = True

dataValid = False

while dataValid == False:
    grade2 = input("Type the grade of the second test: ")
    try:
        grade2 = float(grade2)
    except:
        print(
            "Invalid input. Only numbers are accepted and decimals separated with a dot."
        )
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grade must be between 0 and 10")
        continue
    else:
        dataValid = True

dataValid = False

while dataValid == False:
    totalClasses = (input("Type the number of classes: "))
    try: 
        totalClasses = int(totalClasses)
    except:
        print("Invalid input. Only numbers are accepted and decimals separated with a dot.")
        continue
    if totalClasses <= 0:
        print("Classes cannot be a negative value")
        continue
    else:
        dataValid = True

dataValid = False

while dataValid == False:
    absences = (input("Type the number of absences: "))
    try:
        absences = int(absences)
    except:
        print("Absences must be a positive number")
        continue
    if absences < 0 or absences > totalClasses:
        print(
            "Number of absences cannot be greater than number of classes andmust be between 0 and 20"
        )
        continue
    else:
        dataValid = True

avgGrade = (grade1 + grade2) / 2
attendance = (totalClasses - absences) / totalClasses

# Rules: Grades are 0 to 10
# Approval rate is 6 or higher
# Attendance rate of >= 80%

print("The average grade is: ", round(avgGrade, 2))
print("Attendance Rate: ", str(round(attendance * 100, 2)) + "%")

if avgGrade >= 6:
    if attendance > 0.8:
        print("Congratulations, this student is approved!")
    else:
        print(
            "Unfortunately this student has failed due to an attenance rate lower than 80%"
        )
elif attendance > 0.8:
    print("This student has failed due to a grade lower than 6")
else:
    print(
        "This student has failed due to an attenance rate lower than 80% and a grade lower than 6"
    )

# Using And/OR
# # Ask for grades of two tests made by students
# grade1 = float(input("Type the grade of the first test: "))
# grade2 = float(input("Type the grade of the second test: "))
# absences = float(input("Type the number of absences: "))
# totalClasses = float(input("Type the number of classes: "))

# avgGrade = (grade1 + grade2) / 2
# attendance = (totalClasses - absences) / totalClasses

# # Rules: Grades are 0 to 10
# # Approval rate is 6 or higher
# # Attendance rate of >= 80%

# print("The average grade is: ", round(avgGrade, 2))
# print("Attendance Rate: ", str(round(attendance * 100, 2)) + "%")

# if avgGrade >= 6 and attendance >= 0.8:
#     print("Congratulations, this student is approved!")
# elif avgGrade < 6 and attendance < 0.8:
#     print(
#         "This student has failed due to an attenance rate lower than 80% and a grade lower than 6"
#     )
# elif attendance >= 0.8:
#     print("This student has failed due to a grade lower than 6")
# else:
#     print("This student has failed due to an attenance rate lower than 80%")
