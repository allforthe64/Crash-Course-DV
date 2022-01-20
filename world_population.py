import json
from pygal_maps_world.maps import World 

from country_code import getCountryCode

#load the data into a list
filename = "population_data.json"
with open(filename) as f:
    popData = json.load(f)

#build a population dictionary for the world super powers
supersPopulation = {}
for popDict in popData:
    countryName = popDict["Country Name"]
    countrySign = popDict["Country Code"]
    population = popDict["Value"]

    code = getCountryCode(countryName)

    if code:
        supersPopulation[code] = population
    else:
        print(f"Error - {countryName}")

wm = World()
wm.title = "World super power populations in 2020"

for i in supersPopulation:
    holderDict = {i: supersPopulation[i]}
    String = f"{i}: {supersPopulation[i]}"
    wm.add(String, holderDict)

wm.render_to_file("map.svg")