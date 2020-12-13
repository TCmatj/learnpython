import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'plot//sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))
    
fig = plt.figure(dpi=100,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.title("Daily high and low temperatures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16,alpha=0.5)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.show()