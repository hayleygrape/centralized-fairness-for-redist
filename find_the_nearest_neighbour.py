import numpy as np
import json
import os
import time
import matplotlib.pyplot as plt




distances = np.load('unweighted.npy')
distances = 0.5*np.square(distances)

#
print('done 1')


# draw the histogram 
# NumBins = 20 
# plt.hist(distances,bins=NumBins) 
# plt.title("histogram") 
# plt.show()


# find the nearest neighbour 
numMaps = 50000

closestMapIndex = np.argmin(distances)
closestMapDistance = np.min(distances)
assert closestMapDistance == distances[closestMapIndex]

print('closestMapIndex =%d' % closestMapIndex)
print('closestMapDistance = %f' % closestMapDistance)

# closestMapIndex = 18138
# closestMapDistance =  1109348.278325

