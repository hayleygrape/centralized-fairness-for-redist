import numpy as np
import json
import os
import time
import matplotlib.pyplot as plt


def unweightedDistance(matrix, centroid):

    diff = np.linalg.norm(centroid-matrix)

    return diff



def weightedDistance(w, a1, a2):
    
    diff = np.square(a1-a2)
    w = np.outer(w,w)
    diff_weighted = diff * w
    distance = 0.5 * (diff_weighted.sum())
    
    return distance

centroid = np.load('centroid.npy')

print(np.shape(centroid))

n=10000 

# thresh is a thresholded map of the centroid 
thresh = np.zeros((n,n))

for i in range(n):
	for j in range(n):
		if centroid[i,j] >= 0.5:
			thresh[i,j] =1 
		else:
			thresh[i,j] =0 


''' 
Find w  and give it to the function below
'''

w = np.load("weights.npy")


dist_to_thresh = weightedDistance(w, thresh, centroid)



print('dist_to_thresh = %f' %dist_to_thresh)

# uniform: dist_to_thresh = 551389.187285
# unform closest: 1109348
# weighted closest: 1109348


## prints below as a check 
# print(centroid[0:10,0:10])
# print(thresh[0:10,0:10])
# print(d)
# print(0.5*(d**2))



