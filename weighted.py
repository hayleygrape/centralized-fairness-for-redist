import numpy as np
import json
import os
import time

start = time.time()

progressdir = "./Progress2/"
os.makedirs(os.path.dirname(progressdir + "init.txt"), exist_ok = True)
with open(progressdir + "init.txt", "w") as f:
    f.write("Created Folder")

centroid = np.load("centroid.npy")

numGraphs = 1000
numDistricts = 18

indices = {}
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

#save indices hashmap for reference later

with open("indexmap.json", "w") as f: 
    json.dump(indices, f)

with open("./Data/PA_VTDALL.json") as f:
    a = json.load(f)

popmap = {}

for node in a['nodes']:
    vtd_id = node["id"]
    pop = node["TOT_POP"]
    index = indices[vtd_id]
    popmap[index] = pop


w = np.zeros(10000)

for i in range(len(w)):
    if i in popmap:
        pop = popmap[i]
    else:
        pop = 0

    w[i] = pop

def weightedDistance(w, a1, a2):
    
    diff = np.square(a1-a2)
    w = np.outer(w,w)
    diff_weighted = diff * w
    distance = 0.5 * (diff_weighted.sum())
    
    return distance

weighted = np.zeros(50000)

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
    
    dist = weightedDistance(w, centroid, temp)
    weighted[i-1] = dist

    if i % 5000 == 0:
        os.makedirs(os.path.dirname(progressdir + "distance" + str(i) + ".txt"), exist_ok = True)
        with open(progressdir + "distance" + str(i) + ".txt", "w") as f:
            f.write("Time elapsed: " + str((time.time()-start)/60) + " minutes")

np.save("weighted.npy", weighted)
print("weighted distances saved in " + str((time.time()-start)/60) + " minutes")