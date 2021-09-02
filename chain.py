import matplotlib.pyplot as plt
from gerrychain import (GeographicPartition, Partition, Graph, MarkovChain, proposals, updaters, constraints, accept, Election,)
from gerrychain.proposals import recom
from gerrychain.updaters import cut_edges
from functools import partial
import pandas
import networkx as nx
import os
import json
import geopandas as gpd
from gerrychain.tree import recursive_tree_part
from gerrychain.constraints import Validator
import time

start = time.time()

newdir = "./Maps/"
os.makedirs(os.path.dirname(newdir + "init.txt"), exist_ok = True)
with open(newdir + "init.txt", "w") as f:
    f.write("Created Folder")

'''
#networkx graph
graph = Graph.from_json("./Data/PA_VTDALL.json")
'''

#make networkx graph
graph = Graph.from_file("./Data/VTD_FINAL.shp")

#make geopandas dataframe
df = gpd.read_file("./Data/VTD_FINAL.shp")

num_districts = 19

initial_partition = Partition(graph, "2011_PLA_1")

print(initial_partition)

totpop = 0
for n in graph.nodes():
    totpop += graph.nodes[n]["TOT_POP"]

ideal_population = totpop / len(
    initial_partition
)
print(ideal_population)


proposal = partial(
    recom, 
    pop_col="TOT_POP",
    pop_target=ideal_population,
    epsilon=0.02,node_repeats=1
    )

compactness_bound = constraints.UpperBound(
    lambda p: len(p["cut_edges"]), 2 * len(initial_partition["cut_edges"])
)


chain = MarkovChain(
    proposal=proposal,
    constraints=[
        compactness_bound
    ],
    accept=accept.always_accept,
    initial_state=initial_partition,
    total_steps=10000
)

jsondir = "./JSON_Files/"
os.makedirs(os.path.dirname(jsondir + "init.txt"), exist_ok = True)
with open(jsondir + "init.txt", "w") as f:
    f.write("Created Folder")

t = 1
mapNum = 1

for partition in chain:
    if t % 100 == 0:
        
        #df['current'] = df["CD_2011"].map(dict(partition.assignment))

        #df.plot(column='current',cmap='tab20')
        #plt.savefig(newdir + "plot" + str(t) + ".png")
        #plt.close()
        #print("plot " + str(t) + " saved")

        partition.graph.to_json(jsondir + "plot" + str(mapNum) + ".json")

        print("JSON for " + str(mapNum) + " saved")

        mapNum += 1

    t += 1

end = time.time()
timeElapsed = (end-start) // 60 #minutes
print("Took " + str(timeElapsed) + " minutes")