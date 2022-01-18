import csv

#get TMAX out of file
filename = "sitka_weather_2018_full.csv"
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    highs = []
    for row in reader:
        highs.append(row[1])

    print(highs)
