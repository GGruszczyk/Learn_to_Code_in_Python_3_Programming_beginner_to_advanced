"""
set of operations to reuse and invoke when needed
def <functionName>(<args>=defaultValue):
  code to execute
  defaultValue omits parameter

  arguments make fx(s) dynamic
"""


# define
def sayHello(person, person2="The Director"):
    print("Hello!", person, "how are you doing? " + person2 + " is waiting for you")


# invoke
sayHello("Kris", "Austin")  # input used to assign value to person args
sayHello("Austin")  # input used to assign value to person, using person2 default
sayHello("Graig", "Kris")

print(5, "Hello", ["Time", "To Make a List"])
print(float(3))
print(type(False))
print(round(3.6746, 2))

# ctrl + ` to switch cursor between terminal and editor


# this fx converts a temp from fahr to celsius 'return' allows you to dyanmically enter the value
#
def far2celsius(fahr):
    celsius = 5 * (fahr - 32) / 9
    return celsius


# convert 100 degrees far to other temperatures and round
print("Celsius: ", round(far2celsius(100), 2))
print("Kelvin: ", round(far2celsius(100) + 273.5, 2))
