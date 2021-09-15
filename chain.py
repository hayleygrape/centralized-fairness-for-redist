import matplotlib.pyplot as plt
from gerrychain import (GeographicPartition, Partition, Graph, MarkovChain, proposals, updaters, constraints, accept, Election,)
from gerrychain.proposals import recom
from gerrychain.updaters import Tally
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


#networkx graph
graph = Graph.from_json("./Data/PA_VTDALL.json")


#make networkx graph
#graph = Graph.from_file("./Data/VTD_FINAL.shp")

#make geopandas dataframe
df = gpd.read_file("./Data/VTD_FINAL.shp")

num_districts = 18

#election updater
elections = [
    Election("PRES16", {"D": "T16PRESD", "R": "T16PRESR"}),
    Election("SEN16", {"D": "T16SEND", "R": "T16SENR"}),
    Election("AG16", {"D": "T16ATGD", "R": "T16ATGR"}),
    Election("GOV14", {"D": "F2014GOVD", "R": "F2014GOVR"})
]

electionNames = ["PRES16", "SEN16", "AG16", "GOV14"]

parties = ["D", "R"]

updaters = {
    "population": updaters.Tally("TOT_POP", alias="population")
}

election_updaters = {election.name: election for election in elections}
updaters.update(election_updaters)

initial_partition = Partition(graph, "2011_PLA_1", updaters=updaters)


totpop = 0
for n in graph.nodes():
    totpop += graph.nodes[n]["TOT_POP"]

ideal_population = totpop / len(
    initial_partition
)

proposal = partial(
    recom, 
    pop_col="TOT_POP",
    pop_target=ideal_population,
    epsilon=0.02,
    node_repeats=1
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
    total_steps=50000
)

jsondir = "./JSON_Files/"
os.makedirs(os.path.dirname(jsondir + "init.txt"), exist_ok = True)
with open(jsondir + "init.txt", "w") as f:
    f.write("Created Folder")

t = 1
mapNum = 1

for partition in chain:
    if t % 1 == 0:
        
        df["plot" + str(mapNum)] = df["GEOID10"].map(dict(partition.assignment))

        df.plot(column='plot' + str(mapNum),cmap='tab20')
        plt.savefig(newdir + "plot" + str(t) + ".png")
        plt.close()

        d = {}

        for i in range(num_districts):
            d[i+1] = {}

        for district in partition["population"]:
            d[district]["population"] = partition["population"][district]
            d[district]["id"] = []

        for key in partition.assignment:
            district = partition.assignment[key]
            d[district]["id"].append(key)

        
        for electionName in electionNames:

            d[electionName] = {}
            if partition[electionName].votes("D") > partition[electionName].votes("R"):
                d[electionName]["winner"] = "D"
            elif partition[electionName].votes("D") < partition[electionName].votes("R"):
                d[electionName]["winner"] = "R"
            else:
                d[electionName]["winner"] = "TIE"
            
            d[electionName]["D"] = {}
            d[electionName]["R"] = {}

            for party in parties:
                d[electionName][party]["seats"] = partition[electionName].seats(party)
                d[electionName][party]["percent_wins"] = partition[electionName].percent(party)
                d[electionName][party]["votes"] = int(sum(partition[electionName].counts(party)))


        with open(jsondir + "plot" + str(mapNum) + ".json", 'w') as f:
            json.dump(d, f)

        if mapNum % 1000 == 0:
            currTime = time.time()
            timeElapsed = (currTime - start) // 60
            print("JSON for " + str(mapNum) + " saved in " + str(timeElapsed) + " minutes")


        mapNum += 1

    t += 1

end = time.time()
timeElapsed = (end-start) / 60 #minutes
print("Took " + str(timeElapsed) + " minutes")