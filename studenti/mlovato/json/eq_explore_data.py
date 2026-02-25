from pathlib import Path
import json
import plotly.express as px

# get path
path = Path("eq_data/m1_dec13_30_day.geojson")

# read from path with utf-8 encoding
contents = path.read_text(encoding="utf-8")
# decode json data
all_eq_data = json.loads(contents)

# esamina tutti i terremoti del dataset

all_eq_dict = all_eq_data["features"]

mags,lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dict:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    eq_titles.append(eq_dict["properties"]["title"])

title = all_eq_data["metadata"]["title"]

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, color_continuous_scale="inferno", labels={"color":"Magnitude"}, projection="natural earth", hover_name=eq_titles,)
fig.show()
