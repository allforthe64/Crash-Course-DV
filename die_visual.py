import pygal
from die import Die

#create a D6 and D10
die = Die()
die1 = Die(10)

#make some rolls and store results in a list
results = []

for i in range(50000):

    result = die.roll() + die1.roll()
    results.append(result)

#analyze the results
frequencies = []
maxResult = die.numSides + die1.numSides
for i in range(2, maxResult + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

#visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file("die_visual.svg")