# **********************************************************************
#
# Example name: Web Scraper
# Description: Read data from html tags and write into a csv file.
# https://www.boxofficemojo.com/year/world/?ref_=bo_nb_hm_tab
#
# **********************************************************************
from os import path
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


def main():
    url = "https://www.boxofficemojo.com/month/?ref_=bo_nb_hm_secondarytab"
    response = urlopen(url)
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    tables = soup.find_all("table")
    ths = tables[0].find_all("th")
    header = get_table_row(ths)
    table_data = []

    for table in tables:
        trs = table.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            if len(tds) == len(header):
                table_data.append(get_table_row(tds))

    dataframe = pd.DataFrame(table_data, columns=header)
    dataframe.to_csv(path.abspath(path.join("..", "out", "test.csv")))


def get_table_row(cells):
    return [td.getText().strip() for td in cells]

if __name__ == '__main__':
    main()