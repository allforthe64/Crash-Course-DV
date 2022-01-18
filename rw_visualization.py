import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making random walks while the program is running
while True:
    rw = RandomWalk(50000)
    rw.fillWalk()

    #add color map and plot points
    pointNumbers = list(range(rw.numPoints))
    plt.scatter(rw.xValues, rw.yValues, c=pointNumbers, cmap=plt.cm.viridis, s=1)
    plt.savefig("RandWalk.png")

    #add emphasis to the first and last points
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.xValues[-1], rw.yValues[-1], c="red", edgecolors="none", s=100)

    keepRunning = input("Make another walk? (y/n): ")
    if keepRunning == "n":
        break

