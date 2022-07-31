# **********************************************************************
#
# Example name: OSM Data collector
# Description: How to write a csv file by fetching data from osm search
#
# **********************************************************************
import json
import re
import ssl
from urllib.request import urlopen

import certifi
import pandas as pd

location_list = ((35.71824, 51.42025), (35.70627, 51.42922), (35.69379, 51.39526), (35.71616, 51.40423))
data = {"lon": [], "lat": [], "display_name": []}

for y, x in location_list:
    url = "https://nominatim.openstreetmap.org/search.php?q={0},{1}&format=jsonv2".format(y, x)
    url_result = urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
    json_results = json.loads(url_result.read())

    for json_result in json_results:
        display_name = json_result['display_name']
        lat = json_result['lat']
        lon = json_result['lon']
        data["lat"].append(lat)
        data["lon"].append(lon)
        data["display_name"].append(display_name)

df = pd.DataFrame(data)
df.to_csv("out.txt", encoding="utf-8")
