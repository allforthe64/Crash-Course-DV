import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

#Set the chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set the size of the tick lables
plt.tick_params(axis="both", which="major", labelsize=14)

plt.savefig("Output.png")