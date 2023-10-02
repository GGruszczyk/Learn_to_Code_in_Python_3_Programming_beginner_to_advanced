# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

plt.plot(x, y)
plt.show

legend = ["January", "February", "March", "April"]
# assigns function to element
plt.xticks()

# replace numeric value with strings (not showing)
plt.plot(legend)
plt.show()

plt.bar(x, y)
plt.ylabel("Sales in $US")
plt.title("Monthly Sales")
plt.show()

# Reference https://matplotlib.org/stable/index.html
