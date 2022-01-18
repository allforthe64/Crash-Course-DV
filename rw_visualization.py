import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making random walks while the program is running
while True:
    rw = RandomWalk()
    rw.fillWalk()

    plt.scatter(rw.xValues, rw.yValues, s=1)
    plt.savefig("RandWalk.png")

    keepRunning = input("Make another walk? (y/n): ")
    if keepRunning == "n":
        break

