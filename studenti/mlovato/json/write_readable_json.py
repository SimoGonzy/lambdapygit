from pathlib import Path
import json

# get path
path = Path("eq_data/eq_data_1_day_m1.geojson")

# read from path with utf-8 encoding
contents = path.read_text(encoding="utf-8")
# decode json data
all_eq_data = json.loads(contents)

# crea una versione leggibile
# set up the path where to store new readable data
path = Path("eq_data/eq_data_readable_1_day_m1.geojson")
# encoce in json the all_eq_data (the dictionary we have) with identation
readable_content = json.dumps(all_eq_data, indent=4)
# write the encoded json file with identation in the path file
path.write_text(readable_content)