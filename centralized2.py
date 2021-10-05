import json
import os
import time
import numpy as np
from itertools import combinations

start = time.time()

numGraphs = 50000
numDistricts = 18

#create 10,000 x 10,000 array filled with zeros
centroid = np.zeros((10000, 10000))

#since nodes are labeled by their node ID which is a combo of
#numbers and letters, i created this dictionary to id them by integers to insert them 
#into centroid array

indices = {}

progressdir = "./Progress/"
os.makedirs(os.path.dirname(progressdir + "init.txt"), exist_ok = True)
with open(progressdir + "init.txt", "w") as f:
    f.write("Created Folder")

matdir = "./Matricies/"
os.makedirs(os.path.dirname(matdir + "init.txt"), exist_ok = True)
with open(matdir + "init.txt", "w") as f:
    f.write("Created Folder")

districts = [str(x+1) for x in range(numDistricts)]

t = 0

fdir = "./JSON_Files2/plot1.json"
with open(fdir) as a:
    dict1 = json.load(a)

#numbering the districts
for district in districts: 
    for node in dict1[district]["id"]:
        if node not in indices:
            indices[node] = t
            t += 1

for i in range(2000, numGraphs+1): #since I labeled the json files using 1 indexing

    fdir = "./JSON_Files2/plot" + str(i) + ".json"
    with open(fdir) as a:
        dict1 = json.load(a)

    temp = np.zeros((10000, 10000))

    for district in districts:
        sameDist = dict1[district]["id"] #array of all the nodes in the same district

        length = len(sameDist)

        row = np.zeros(10000)

        for node in sameDist:
            index = indices[node]
            row[index] = 1

        for node in sameDist:
            temp[indices[node]] = row

    if i % 1000 == 0:
        os.makedirs(os.path.dirname(progressdir + "map" + str(i) + ".txt"), exist_ok = True)
        with open(progressdir + "map" + str(i) + ".txt", "w") as f:
            f.write("Time elapsed: " + str((time.time()-start)/60) + " minutes")

    #np.save(matdir + "matrix" + str(i) + ".npy", temp)

    centroid = centroid + temp

#divide every entry by number of graphs
centroid /= (numGraphs-1999)

np.save("centroid.npy", centroid)

currTime = time.time()
print("Centroid calculated")
print("Time elapsed so far: " + str((currTime-start) / 60) + " minutes")

'''
minDistance = float('inf')
distances = []

while len(stack) != 0:

    matrix = stack.pop()

    dist = np.linalg.norm(centroid-matrix)
    distances.append(round(dist, 2))
    
    if dist < minDistance:
        minDistance = dist

end = time.time()
print("Done")
timeElapsed = (end - start) / 60 #in minutes
print("Took " + str(timeElapsed) + " minutes")
print("Distances array: ")
print(distances)
print("Min Difference = " + str(round(minDistance, 2)))
'''