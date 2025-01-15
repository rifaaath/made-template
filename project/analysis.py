import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load world shapefile
world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")

# Load your cleaned data (GDP and enrollment)
education_data = pd.read_csv("data/data1.csv")
gdp_data = pd.read_csv("data/data2.csv")

# Ensure consistent column naming
columns = ["Country Name"] + [str(year) for year in range(1970, 2024)]
education_data = education_data[columns]
gdp_data = gdp_data[columns]

# Merge with geographical data
# Focus only on the Americas
americas = [
    "United States", "Canada", "Mexico", "Guatemala", "Honduras", 
    "Costa Rica", "Brazil", "Argentina", "Colombia", "Chile"
]
education_data["Enrollment_Mean"] = education_data.loc[:, "1970":"2023"].mean(axis=1)
gdp_data["GDP_Mean"] = gdp_data.loc[:, "1970":"2023"].mean(axis=1)

data = pd.merge(education_data[["Country Name", "Enrollment_Mean"]],
                gdp_data[["Country Name", "GDP_Mean"]],
                on="Country Name")

# Merge with GeoDataFrame
geo_data = world[world["ADMIN"].isin(americas)]
geo_data = geo_data.merge(data, left_on="ADMIN", right_on="Country Name", how="left")

# Plotting the data
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
geo_data.plot(column='Enrollment_Mean', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
plt.title("Primary School Enrollment Rates in the Americas (1970-2023)", fontsize=16)
plt.show()

# Masking to highlight the Americas
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
world.boundary.plot(ax=ax, color="gray", linewidth=0.5)  # Background map
geo_data.plot(column='GDP_Mean', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
plt.title("GDP Per Capita in the Americas (1970-2023)", fontsize=16)
plt.show()
