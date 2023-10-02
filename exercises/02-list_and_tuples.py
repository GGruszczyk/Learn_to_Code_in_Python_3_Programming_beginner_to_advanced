# IDLE practice
# Lists
# students = "John, Mary, Steve"
# #lists and tuples (arrays) adding or removing from
# students = ["John", "Mary", "Steve"]
# type(students)
# <class 'list'>
# len(students)
# 3
# students[0]
# 'John'
# Grab the last student and the last two
# students[2] || students[-1] (dynamic)
# 'Steve'
# students[-2:]
# ['Mary', 'Steve']
# students.append("Kate") #adds to the end
# students.insert(0, "Kris") # (position, value)
# students
# ['Kris', 'George', 'Mary', 'Steve', 'Kate']
# students.pop() # removes from the end by default
# 'Kate'
# students
# ['Kris', 'George', 'Mary', 'Steve']
# students.pop(1)
# 'George'
# students
# ['Kris', 'Mary', 'Steve']
# students.remove("Mary") # removes the first element if two are present
# students
# ['Kris', 'Steve']
# students2 = ["Paul", "John"]
# merging
# students + students2
# ['Kris', 'Steve', 'Paul', 'John']

# Tuples (immutable, safer for more complex programs)
# ex: months of the year
# months = ("January", "Februrary", "March")
# type(months)
# <class 'tuple'>
# months[0]
# 'January'
# len(months)
# 3

# **REVISIT** ask for the user's birthday using DD-MM-YYYY format
# print the corresponding month from the tuple ex: Your birthday is in <month name>
# my solution
# import calendar
# userMonth = input(print("Please enter your birthday using the following format DD-MM-YYYY"))
# monthByNumber = (1,2,3,4,5,6,7,8,9,10,11,12)
# print(calendar.month_name(userMonth))
# *TALK THROUGH*

months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

birthday = input("Please type your birthday using the format: DD-MM-YYYY ")
index = int(birthday[3:5]) - 1  # birthday[included:excluded]
bd_month = months[index]
print("You were born in:", bd_month)

indexYear = birthday[-1:-5]
print("You were born in the year: ", indexYear)

# create a predefined list of people
# prompt the user to enter their name add it to the end of the list and print the updated list
# listOfPeople = ["Kat", "Grey", "Anthony", "Thomas", "Tim", "Tom", "Ted"]
# userNameInput = input(print("Please enter your name:"))
# listOfPeople.append(userNameInput)
# print("Welcome", userNameInput + "!", "You've been added to the list", listOfPeople)
# Resources: https://docs.python.org/3/library/calendar.html

# Next commit:
# made file names more consistent
