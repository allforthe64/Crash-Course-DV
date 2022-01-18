import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a random walk and plot the points
rw = RandomWalk()
rw.fillWalk()

plt.scatter(rw.xValues, rw.yValues, s=1)
plt.savefig("RandWalk.png")

