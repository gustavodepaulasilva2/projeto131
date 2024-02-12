import pandas as pd

planet_df = pd.read_csv("\Downloads\projeto-127\scraped_data.csv")
new_planet_df = pd.read_csv("\Downloads\projeto-127\new_scraped_data.csv")

for planet_data in planet_df, new_planet_df:
  if planet_data.lower() == "unknown":
    planet_data.remove(planet_data)

new_temp_list = []

for planet_data in new_temp_list:

  planet_mass = planet_data[5]

  if planet_mass.lower() == "unknown":
    new_temp_list.remove(planet_data)
    continue
  else:
    planet_mass= float(planet_mass) * 0.000954588
    planet_data[3] = planet_mass

  planet_radius = planet_data[6]

  if planet_radius.lower() == "unknown":
    new_temp_list.remove(planet_data)
    continue
  else:
    planet_radius = float(planet_radius) * 0.102763
    planet_data[7] = planet_radius

headers = ["Star_name","Distance","Mass","Radius","Lum"]
star_df_1 = pd.DataFrame(new_temp_list,columns = headers)

star_df_1.to_csv("Merge_scraped_data.csv", index=True, index_label="id")