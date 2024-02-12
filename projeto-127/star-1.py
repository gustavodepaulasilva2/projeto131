from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import pandas as pd

scraped_data = []



startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get(startUrl)

time.sleep(10)


def scraper():
    soup = BeautifulSoup(driver.page_source,"html.parser")
    bright_star_table = soup.fing("table", attrs={"class","wikitable"})
    table_boby = bright_star_table.find("tbody")
    table_rows = table_boby.find_all("tr")
    for row in table_rows:
        table_cols = row.find_all("td")
        temp_list = []
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)

stars_data = []

for i in range(0,len(scraped_data)):
    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][1]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_name,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

headers = ["Star_name","Distance","Mass","Radius","Lum"]
star_df_1 = pd.DataFrame(stars_data,columns = headers)

star_df_1.to_csv("scraped_data.csv", index=True, index_label="id")
