# # structures of repetition
# # x += 1 increment operator

# # generate a list of elements based on user input
# # print out the list
# people = []

# while len(people) < 5:
#     # ask user to enter person's name
#     person = input("Type the name of a person: ")
#     # add person to list
#     people.append(person)
# print(people)

# guess game for a random number
import random

number = random.randint(0, 10)

guess = int(input("I'm thinking of a number. Can you guess it? "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope. Try again."))
print("You guessed it. The number was ", number)

# learned about conditionals starting with "while"
