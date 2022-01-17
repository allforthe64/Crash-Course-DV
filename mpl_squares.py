import matplotlib.pyplot as plt

inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(inputs, squares, linewidth=5)

#add labels to the graph
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set the size of tick labels

plt.savefig("Output.png")