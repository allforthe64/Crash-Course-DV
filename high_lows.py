import csv

#get TMAX out of file
filename = "sitka_weather_2018_full.csv"
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    highs = []
    highsActual = []
    for row in reader:
        highs.append(row[8])
        
    
    for i in highs:
        if not i:
            pass
        else:
            highsActual.append(int(i))
    
print(highsActual)
