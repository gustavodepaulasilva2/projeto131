import pandas as pd

planet_df = pd.read_csv("\Downloads\projeto-127\scraped_data.csv")
for planet in planet_df:
    planet_df.drop(columns=[7])

planet_df.describe()
planet_df.info()
planet_df.dtypes

headers = ["Star_name","Distance","Mass","Radius","Lum"]
new_planet_df_1 = pd.DataFrame(planet_df, columns = headers)
new_planet_df_1.to_csv('final_scraped_data.csv', index=True, index_label="id")