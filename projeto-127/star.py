from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

new_scraped_data = []



startUrl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get(startUrl)

time.sleep(10)


def scraper_more_data(hiper_link):
    try:
        page = requests.get(hiper_link)
        soup = BeautifulSoup(page.content,"html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr", attrs={"class","wikitable"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("a",attrs={"class","wikitable"})[0].contents[0])
                except:
                    temp_list.append("")
        new_scraped_data.append(temp_list)
    except:
        time.sleep(1)
        scraper_more_data(hiper_link)
        
for i in range(scraper_more_data):
    Star_name = new_scraped_data[i][1]
    Distance = new_scraped_data[i][1]
    Mass = new_scraped_data[i][5]
    Radius = new_scraped_data[i][6]
    Lum = new_scraped_data[i][7]

    required_data = [Star_name,Distance,Mass,Radius,Lum]
    new_scraped_data.append(required_data)

ajusted_data =[]
for row in new_scraped_data:
    replaced = []
    for element in row:
        element = element.replace("\n","")
        replaced.append(element)
    ajusted_data.append(replaced)
print(ajusted_data)

headers = ["Star_name","Distance","Mass","Radius","Lum"]
new_planet_df_1 = pd.DataFrame(ajusted_data, columns = headers)
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
