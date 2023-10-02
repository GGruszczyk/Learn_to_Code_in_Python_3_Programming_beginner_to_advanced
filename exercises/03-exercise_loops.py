# Create a program that asks the user for 9 names of people and stores them in a list. When all the names have been given, pick a random one and print it.
# create empty list for names
import random

# # solution
people = []

for x in range(0, 8):
    person = input("Type the name of a person: ")
    people.append(person)
index = random.randint(0, 7)

random_person = people[index]

print("Let's pick a random person: ", random_person)

# first attempt

# while len(people) <= 1:
#     person = input("Please type the name of a person: ")
#     people.append(person)
# print(people)

# 2nd attempt

# Create a guess game with the names of the colors. At each round, pick a random color from a list and let the user try to guess it. When they do, ask if they want to play again. Keep playing until the user types "no"

# colors = ["Yellow", "Orange", "Blue", "Red"]

# import random

# while True:
#     # returns a random number dynamically based on size of the list
#     color = colors[random.randint(0, len(colors) - 1)].lower()
#     guess = input("Can you guess the color I'm thinking of? ")

#     while True:
#         if color == guess:
#             break
#         else:
#             guess = input("Nope. Try again. ")

#     print("You guessed it! I was thinking about", color)

#     play_again = input("Let's play again? Type 'no' to quit.")

#     if play_again.lower() == "no":
#         break
# print("Thanks for playing!")

# # backend engineers create servers to work with SQL and websites 1. data extraction and computation 2. automating small tasks
# # data engineer machine learning (ML) creating data pipelines and warehouses for data scientists for learning purposes
# # rba automation anywhere using drag and drop developer creating columns in excel for data crunching when users download information from website
