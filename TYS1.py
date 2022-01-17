'''Plot the numbers 1-5 cubed, then plot the numbers between 1-5000 cubed'''

import matplotlib.pyplot as plt

'''Cube the first five numbers cubed'''
xInputs = [1, 2, 3, 4, 5]
yInputs = [1, 4, 9, 16, 25]

#apply color to graph and graph the numbers
plt.scatter(xInputs, yInputs, c=yInputs, cmap=plt.cm.viridis)

#Set the chart title and label axes
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.savefig("Output.png")

'''Cube all numbers between 1 and 5000'''
xInputs = list(range(1, 5001))
yInputs = [x**3 for x in xInputs]

#apply color to graph and graph the numbers
plt.scatter(xInputs, yInputs, c=yInputs, cmap=plt.cm.viridis)

#Set the chart title and label axes
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.savefig("Output1.png")