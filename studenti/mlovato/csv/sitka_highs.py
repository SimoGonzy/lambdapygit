import csv
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_simple.csv")

lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
# legge la prima riga
header_row = next(reader)

dates, highs = [], []
# riprende a leggere da dove ha iniziato
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# plotta le temperature
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
fig.autofmt_xdate()

# cambiare le label
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()