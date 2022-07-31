# **********************************************************************
#
# Example name: Web Scraper
# Description: Read data from html tags and write into a csv file.
# https://www.boxofficemojo.com/year/world/?ref_=bo_nb_hm_tab
#
# **********************************************************************
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.boxofficemojo.com/month/?ref_=bo_nb_hm_secondarytab"
response = urlopen(url)
content = ''
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
tables = soup.find_all("table")

header = ["Year",
          "Cumulative Gross",
          "%± LY",
          "Releases",
          "Average",
          "#1 Release",
          "# Gross",
          "# % of Total"]

table_data = {
    "Year": [],
    "Cumulative Gross": [],
    "%± LY": [],
    "Releases": [],
    "Average": [],
    "#1 Release": [],
    "# Gross": [],
    "# % of Total": []
}

for table in tables:
    trs = table.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) >= len(header):
            table_data["Year"].append(tds[0].getText().strip())
            table_data["Cumulative Gross"].append(tds[1].getText().strip())
            table_data["%± LY"].append(tds[2].getText().strip())
            table_data["Releases"].append(tds[3].getText().strip())
            table_data["Average"].append(tds[4].getText().strip())
            table_data["#1 Release"].append(tds[5].getText().strip())
            table_data["# Gross"].append(tds[6].getText().strip())
            table_data["# % of Total"].append(tds[7].getText().strip())

dataframe = pd.DataFrame(table_data)
print(dataframe)
