import json

#load the data into a list
filename = "population_data.json"
with open(filename) as f:
    popData = json.load(f)

#print the population for each country
for popDict in popData:
    countryName = popDict["Country Name"],
    countrySign = popDict["Country Code"]
    population = popDict["Value"]

    print(f"Name: {countryName}, Population: {population}, Symbol: {countrySign}")