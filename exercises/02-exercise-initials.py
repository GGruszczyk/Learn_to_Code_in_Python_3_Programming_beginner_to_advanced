#Data types: string = sequence of characters
# invoice number, zip code
# len -1 gives last character
# splicing myString[start:finish] can omit or leave off like this myString[-2:] grabs last two

#Create a program that asks for the users full name and then returns their intials

firstName = input("What is your first name?")
middleName = input("What is your middle name?")
lastName = input("What is your last name?")

print("Your initials are: ", firstName[0], middleName[0], lastName[0])

# Concatenation
"user" + str(22)  # user22