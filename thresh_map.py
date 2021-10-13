import numpy as np
import json
import os
import time
import matplotlib.pyplot as plt


def unweightedDistance(matrix, centroid):

    diff = np.linalg.norm(centroid-matrix)

    return diff


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




dist_to_thresh = unweightedDistance(thresh,centroid) 
dist_to_thresh = 0.5*(dist_to_thresh**2)

print('dist_to_thresh = %f' %dist_to_thresh)

# dist_to_thresh = 551389.187285


## prints below as a check 
# print(centroid[0:10,0:10])
# print(thresh[0:10,0:10])
# print(d)
# print(0.5*(d**2))



