import numpy as np
import json

centroid = np.load("centroid.npy")

numGraphs = 50000
numDistricts = 18

weighted = False

indices = {}

districts = [str(x+1) for x in range(numDistricts)]

t = 0

weightedDistances = np.zeros(50000)
unweightedDistances = np.zeros(50000)

fdir = "./JSON_Files2/plot1.json"
with open(fdir) as a:
    dict1 = json.load(a)

#numbering the districts
for district in districts: 
    for node in dict1[district]["id"]:
        if node not in indices:
            indices[node] = t
            t += 1

def weightedDistance():
    pass

def unweightedDistance(matrix, centroid):

    diff = np.linalg.norm(centroid-matrix)

    return diff

for i in range(1, numGraphs+1):
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
        os.makedirs(os.path.dirname(progressdir + "map2" + str(i) + ".txt"), exist_ok = True)
        with open(progressdir + "map2" + str(i) + ".txt", "w") as f:
            f.write("Time elapsed: " + str((time.time()-start)/60) + " minutes")

    if weighted:
        weightedDistance()

    else:
        dist = unweightedDistance(temp, centroid)
        print(dist)
        unweightedDistances[i-1] = dist

np.save("unweighted.npy", unweightedDistances)
