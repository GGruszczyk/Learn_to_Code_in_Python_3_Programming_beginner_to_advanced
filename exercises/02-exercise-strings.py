# Overview:
# Data types: string = sequence of characters
# invoice number, zip code
# len -1 gives last character
# useful case for alternating quotation marks "She said 'meet me at 5'"
# access an index using braces [] the end of a string using negative #'s
# myString[len(myString)-1] useful in loops
# myString
# splicing myString[start:finish] can omit or leave off like this myString[-2:] grabs last two

# Practice
# myString = "She said"
# len(myString)
# 8
# myString[len(myString)-1]
# 'd'
# myString[0:8]
# 'She said'
# myString[0:2]
# 'Sh'
# myString[2:]
# 'e said'
# myString[-2:]
# 'id'
# myString[:3] (start at the beginning grab the first 3) start from the index we're informing at beginning of the string
# 'She'
# myString[3:] (start at 3 until the end) start from the index we're informing at end of the string
#' said'
# "user" + str(22)
# 'user22'

# Create a program that asks for the users full name and then returns their intials

firstName = input("What is your first name?")
middleName = input("What is your middle name?")
lastName = input("What is your last name?")

print("Your initials are: ", firstName[0], middleName[0], lastName[0])


