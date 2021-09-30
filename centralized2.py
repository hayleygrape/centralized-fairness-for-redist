import json
import os
import time
import numpy as np
from itertools import combinations

start = time.time()

numGraphs = 1000
numDistricts = 18

#create 10,000 x 10,000 array filled with zeros
centroid = np.zeros((10000, 10000))

#since nodes are labeled by their node ID which is a combo of
#numbers and letters, i created this dictionary to id them by integers to insert them 
#into centroid array

indices = {}

matdir = "./Matricies/"
os.makedirs(os.path.dirname(matdir + "init.txt"), exist_ok = True)
with open(matdir + "init.txt", "w") as f:
    f.write("Created Folder")

districts = [str(x+1) for x in range(numDistricts)]

t = 0

for i in range(1, numGraphs+1): #since I labeled the json files using 1 indexing

    fdir = "./JSON_Files2/plot" + str(i+2000) + ".json"
    with open(fdir) as a:
        dict1 = json.load(a)

    temp = np.zeros((10000, 10000))

    for district in districts:
        sameDist = dict1[district]["id"] #array of all the nodes in the same district
        a = combinations(sameDist, 2)
        for pairs in a:

            node1 = pairs[0]
            if node1 not in indices:
                indices[node1] = t
                t += 1

            node2 = pairs[1]
            if node2 not in indices:
                indices[node2] = t
                t += 1   
            
            temp[indices[node1], indices[node2]] = 1 #same district
            temp[indices[node2], indices[node1]] = 1 #should be half filled but can't figure out yet -- filling the whole

    if i % 10 == 0:
        print("Map " + str(i) + " done")

    #np.save(matdir + "matrix" + str(i) + ".npy", temp)

    centroid = centroid + temp

#divide every entry by 2
centroid /= 2

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