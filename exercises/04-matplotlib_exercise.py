"""
Create a program to help the user type faster. Give him a word and ask him to write it five times. 
Check how many seconds it took them to type the word at each round
Lastly, tell the user how many mistakes they made
and show a chart with the typing speed evolution during 5 rounds
"""

# import modules
import matplotlib.pyplot as plt
import time as t

# initialize list for attempts and variable to store errors
times = []
mistakes = 0

print(
    "This program will help you type faster. Please type the word 'programming' fives times as fast as you can."
)

# prompt to continue (don't need a variable b/c only input needed)
input("Please press enter to continue")

# while list is < 5 let's get the time stamp at the start
while len(times) < 5:
    # create variables for start/end times, to hold words typed and calculate time elapsed
    start = t.time()
    words = input("Type the word: ")
    end = t.time()
    # send time elapsed to times list (end loop)
    time_elapsed = end - start
    times.append(time_elapsed)  # missing
    # check if mistakes were made
    if words.lower() != "programming":
        mistakes += 1
# print mistakes (will need to convert to string to avoid numbers in between)
print("You made " + str(mistakes) + " mistake(s).")
# wait 3 seconds to show results
t.sleep(3)
# print results
print("Here is your evolution timeline")
# make a list for the x and y coordinates
x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)
# create a legend to display attempts (as list)
legend = ["1", "2", "3", "4", "5"]
# sets ticks location on chart
plt.xticks(x, legend)
# add labels to x and y axis
plt.xlabel("Time in seconds")
plt.ylabel("Number of attempts")
# add a title
plt.title("This is your evolution timeline:")
# plot them and show them
plt.show()


"""
Create a program to help the user type faster. Give him a word and ask him to write it five times. 
Check how many seconds it took them to type the word at each round
Lastly, tell the user how many mistakes they made
and show a chart with the typing speed evolution during 5 rounds
"""

# Try on your own

# import modules
# initialize list for attempts and variable to store errors
# prompt to continue (don't need a variable b/c only input needed)
# while list is < 5 let's get the time stamp at the start
# create variables for start/end times, to hold words typed and calculate time elapsed
# send time elapsed to times list (end loop)
# check if mistakes were made
# print mistakes (will need to convert to string to avoid numbers in between)
# wait 3 seconds to show results
# print results
# make a list for the x and y coordinates
# create a legend to display attempts (as list)
# sets ticks location on chart
# add labels to x and y axis
# add a title
# plot them and show them
