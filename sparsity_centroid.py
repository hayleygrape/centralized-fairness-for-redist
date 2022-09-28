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




numVTDs = 8921 
#numValidPairs =  (0.5*numVTDs*(numVTDs+1))
numValidPairs = (numVTDs**2) - numVTDs 
centroid = np.load('centroid.npy')
centroid = centroid[0:numVTDs,0:numVTDs]



#print(np.shape(centroid))

threshValue = 0.95
numGreaterThan = (centroid >= threshValue).sum()
numGreaterThan = numGreaterThan - numVTDs 
PerGreaterThan = (numGreaterThan/numValidPairs)*100
print('\n')
print(numValidPairs)
print('numGreaterThan = %d' %numGreaterThan)
print('numGreaterThan Percentage = %f' %PerGreaterThan )

print('\n\n')

# print(np.shape(centroid))

# n=10000 


# weights = np.load('weights.npy')
# print(weights[8999:])
# print((weights >0).sum())



# # thresh is a thresholded map of the centroid 
# thresh = np.zeros((n,n))

# for i in range(n):
# 	for j in range(n):
# 		if centroid[i,j] >= 0.5:
# 			thresh[i,j] =1 
# 		else:
# 			thresh[i,j] =0 




# dist_to_thresh = unweightedDistance(thresh,centroid) 
# dist_to_thresh = 0.5*(dist_to_thresh**2)

# print('dist_to_thresh = %f' %dist_to_thresh)

# # uniform: dist_to_thresh = 551389.187285
# # unform closest: 1109348
# # weighted closest: 1109348


# ## prints below as a check 
# # print(centroid[0:10,0:10])
# # print(thresh[0:10,0:10])
# # print(d)
# # print(0.5*(d**2))



