# **********************************************************************
#
# Example name: Web Scraper
# Description: Read data from html tags and write into a csv file.
# https://www.boxofficemojo.com/year/world/?ref_=bo_nb_hm_tab
#
# **********************************************************************
from os import path

import pandas as pd
from bs4 import BeautifulSoup

input_file = open("index.html", encoding='utf-8')
html_doc = input_file.read()
soup = BeautifulSoup(html_doc, 'html.parser')
tables = soup.find_all("table")
header = [fh.getText().strip() for fh in tables[0].find_all("th")]
table_data = []

for table in tables:
    trs = table.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) == len(header):
            table_data.append([td.getText().strip() for td in tds])

dataframe = pd.DataFrame(table_data, columns=header)
print(dataframe.to_csv(path.abspath(path.join("..", "out", "test.csv"))))
