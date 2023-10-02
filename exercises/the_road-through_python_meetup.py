"""
named after monty python theme holy grail
Intro to python
  built-in
  recursion
  lambda
  user-defined
Object oriented python
TDD with Python
Data science with Python
Parallel distribution with Python Spark
Deep learning & AI Engineering (next meeting)
LOL Code
white boarding to break down your code
"""

import random

class Bear:
    # Build a bear
    def __init__(self, name, arms, legs, body, ears, e_n_m):
        # Basic Build A Bear
        self.name = name
        self.arms = arms
        self.legs = legs
        self.body = int(body)
        self.e_n_m = e_n_m  # eyes nose mouth
        self.ears = ears
        self.energy = 1000

    # New functionality
    def becomeAWrestler(self, costume, moves):
        if costume == "batman" and moves == "climb buildings":
            self.energy += 100
        elif costume == "superman":
            self.energy += 50
        else:
            self.energy -= 75
        print(f"{costume} is {self.energy} level")

    # Basic's for any build a bear
    def walking(self, walking=10):
        if self.legs == "long" and self.body < 5:
            self.energy -= walking
        else:
            self.energy -= walking * 2
        if self.energy < walking:
            print(f"{self.name} cannot walk. Not enough energy")
        else:
            print(f"{self.name} is walking. Energy remaining: {self.energy}")

    # bear eating its own food
    def eating(self, food):
        if food == "honey":
            self.energy += 100
        elif food == "bugs":
            self.energy += 50
        elif food == "berries":
            self.enery += 20
        else:
            print(f"{self.name} doesn't like {food}!")

    # how the bear gets its own food
    def foraging(self):
        # randomly find honey or bugs or berries
        food_options = ["honey", "bugs", "berries", "worms", "tree bark", "a fart"]
        selected_food = random.choice(food_options)
        print(f"{self.name} found {selected_food} while foraging.")
        self.eating(selected_food)
        return selected_food

    # test driven development demo
    def foraging_tdd(self):
        self.something
        something = 0
        return something


# basic unit test
def test_bear_creation():
    # name, arms, legs, body, ears, e_n_m
    bear = Bear("Sir Bear", "short", "long", 10, "round", "blue, black, big")
    assert bear.name == "Sir Bear"
    assert bear.arms == "short"
    assert bear.legs == "long"
    assert bear.body == 10
    assert bear.ears == "round"
    assert bear.e_n_m == "blue, black, big"


# unit testing
def test_foraging():
    bear_foraging = Bear("Sir Bear", "short", "long", 10, "round", "blue, black, big")
    random.seed(0)  # Set a seed for reproducible random choices
    food_found = bear_foraging.foraging()
    assert food_found in ["honey", "bugs", "berries", "worms", "tree bark", "a fart"]


# demo for Test Driven Development
def test_wrestler():
    # costume, moves
    bearCostume = Bear()
    costumeTypes = bearCostume.becomeAWrestler()
    assert costumeTypes in ["superman", "batman", "janitor"]
# def test_foraging_tdd():
# https://github.com/triggxl/build-a-bear/blob/main/bear_test.py