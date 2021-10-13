import numpy as np
import json
import os
import time
import matplotlib.pyplot as plt


NumBins = 10 

distances = np.load('unweighted.npy')

print('done 1')


plt.hist(distances,bins=NumBins) 
plt.title("histogram") 
plt.show()
