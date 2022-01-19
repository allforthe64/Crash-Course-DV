import csv
import matplotlib.pyplot as plt
from datetime import datetime

#get TMAX out of file
filename = "sitka_weather_2018_full.csv"
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    highs = []
    dates = []
    lows = []
    for row in reader:
        highs.append(row[8])
        currentDate = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(currentDate)
        lows.append(row[9])
            

    #plot data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c="red")
    plt.plot(dates, lows, c="blue")

    fig.autofmt_xdate()

    #format plot
    plt.title("Daily high temperatures, July, 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temparature (F)", fontsize=16)
    plt.tick_params(axis="x", which="major", labelsize=16)
    plt.tick_params(axis="y", which="major", labelsize=0)
    
    plt.savefig("high_temps.png")
