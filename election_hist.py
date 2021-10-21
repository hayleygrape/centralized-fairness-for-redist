import numpy as np
import json
import os
import time
import matplotlib.pyplot as plt

numGraphs = 10

sen16 = np.zeros(numGraphs)
pres16 = np.zeros(numGraphs)
ag16 = np.zeros(numGraphs)
gov14 = np.zeros(numGraphs)

start = time.time()

count = 0

for i in range(1, numGraphs+1):
    fdir = "./JSON_Files2/plot" + str(i) + ".json"
    with open(fdir) as a:
        dict1 = json.load(a)

    senSeats = int(dict1["SEN16"]["D"]["seats"])
    presSeats = int(dict1["PRES16"]["D"]["seats"])
    agSeats = int(dict1["AG16"]["D"]["seats"])
    govSeats = int(dict1["GOV14"]["D"]["seats"])

    sen16[i-1] = senSeats
    pres16[i-1] = presSeats
    ag16[i-1] = agSeats
    gov14[i-1] = govSeats

    count += 1

print(str(time.time()-start))

np.save("sen_seats.npy", senSeats)
np.save("pres_seats.npy", presSeats)
np.save("ag_seats.npy", agSeats)
np.save("gov_seats.npy", govSeats)

numBins = [int(i) for i in range(15)]

plt.hist(sen16, bins=numBins, density=True)
plt.savefig("sen16_hist.png")
plt.close()

plt.hist(pres16, bins=numBins, density=True)
plt.savefig("pres16_hist.png")
plt.close()

plt.hist(ag16, bins=numBins, density=True)
plt.savefig("ag16_hist.png")
plt.close()

plt.hist(gov14, bins=numBins, density=True)
plt.savefig("gov14_hist.png")
plt.close()
