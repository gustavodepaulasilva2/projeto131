import pandas as pd

planet_df = pd.read_csv("\Downloads\projeto-127\scraped_data.csv")

planet_gravity = []


for planet_data in planet_df:
  
  planet_mass = planet_data[3]

  if planet_mass.lower() == "unknown":
    planet_df.remove(planet_data)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8
    planet_data[3] = planet_mass_value

    planet_radius = planet_data[7]

  if planet_radius.lower() == "unknown":
    planet_df.remove(planet_data)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
      planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

planet_gravity = []

for index, planet_data in enumerate(planet_df):
  features_list = []
  gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11

planet_df.to_csv("star_with_gravity.csv", index=True, index_label="id")