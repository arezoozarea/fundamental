# **********************************************************************
#
# Example name: OSM Data collector
# Description: How to write a csv file by fetching data from osm search
#
# **********************************************************************
import json
import os
import re
import ssl
from os import path

import certifi
from urllib.request import urlopen

location_list = ((35.71824, 51.42025), (35.70627, 51.42922), (35.69379, 51.39526), (35.71616, 51.40423))
header = "lon,lat,dispaly_name\n"

out_path = path.abspath(path.join('..', 'out'))


if not path.exists(out_path):
    os.mkdir(out_path)

out_file = open(path.join(out_path, 'osm_result.txt'), 'w', encoding='utf8')
out_file.write(header)

for y, x in location_list:
    url = "https://nominatim.openstreetmap.org/search.php?q={0},{1}&format=jsonv2".format(y, x)
    url_result = urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))
    json_results = json.loads(url_result.read())
    for json_result in json_results:
        display_name = re.sub(" *, *", " ", json_result['display_name'])
        lat = json_result['lat']
        lon = json_result['lon']
        content = [lon, lat, display_name]
        out_file.write(','.join(content) + '\n')

out_file.close()

# with open(r"C:\personal_files\tehran_osm_result.txt", 'w', encoding='utf8') as f:
#     f.write(write_result)
