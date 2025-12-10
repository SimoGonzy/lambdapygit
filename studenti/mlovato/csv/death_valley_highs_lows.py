import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime

path = Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
# riprende a leggere da dove ha iniziato
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Dati mancanti per {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# plotta le temperature
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()

# cambiare le label
ax.set_title("Daily High and Lows Temperatures, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()