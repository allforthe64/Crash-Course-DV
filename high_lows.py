import csv
import matplotlib.pyplot as plt

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

    #plot data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(highsActual, c="red")

    #format plot
    plt.title("Daily high temperatures, July, 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temparature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    
    plt.savefig("high_temps.png")

