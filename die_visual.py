from multiprocessing.sharedctypes import Value
from die import Die

#create a D6
die = Die()

#make some rolls and store results in a list
results = []

for i in range(1000):

    result = die.roll()
    results.append(result)

#analyze the results
frequencies = []
for i in range(1, die.numSides + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

print(frequencies)