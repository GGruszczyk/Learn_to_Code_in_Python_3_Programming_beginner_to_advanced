# Ask for grades of two tests made by students
grade1 = float(input("Type the grade of the first test: "))
grade2 = float(input("Type the grade of the second test: "))
absences = float(input("Type the number of absences: "))
totalClasses = float(input("Type the number of classes: "))

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

