import json
import matplotlib.pyplot as plt
import pandas as pd
import os
import geopandas as gpd


df = gpd.read_file("./Data/VTD_FINAL.shp")


numDistricts = 18
mapNum = 10

fdir = "./JSON_Files2/plot" + str(mapNum) + ".json"

with open(fdir) as a:
    dict1 = json.load(a)


districts = [str(x+1) for x in range(numDistricts)]
print(districts)

partition_assignment = {}

for district in dict1:
    if district in districts:
        for vtd_id in dict1[district]["id"]:
            partition_assignment[vtd_id] = int(district)

print(partition_assignment)

df["plot" + str(mapNum)] = df["GEOID10"].map(partition_assignment)

df.plot(column='plot' + str(mapNum),cmap='tab20')
plt.savefig("plot" + str(mapNum) + "_photo.png")
plt.close()
