import matplotlib.pyplot as plt
import numpy as np

# x-axis values
x = [1, 2, 3]
# y-axis values
y = [2, 3, 4]

xx = np.linspace(-5, 5, 11)
plt.plot(xx, xx + 1, ':b', label='y=x+1')
# x = [1,1,2,4,3]
# y = [0,1,1,1,2]

# plotting points as a scatter plot
plt.scatter(x, y, label="points", color="red", marker="x", s=30)

plt.axis([0, max(x) + 1, 0, max(y) + 1])
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('Scatter Plot')
# showing legend
plt.legend()
# function to show the plot
plt.grid()
plt.show()
