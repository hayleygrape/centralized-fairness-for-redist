import numpy as np
import json
import os
import time
import matplotlib.pyplot as plt

def weightedDistance(weight, A1, A2):

	Diff = np.square(A1-A2)
	W = np.outer(weight,weight)
	Diff_weighted = Diff * W
	Distance = 0.5*(Diff_weighted.sum())  

	return Distance


A1= np.array([[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]])

A2= np.array([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]])


# try sets of weights  
unif = np.ones((2,2))
weights = np.array([2,3,1,5]) 

print(weightedDistance(weights,A1,A2))
print(weightedDistance(unif,A1,A2))

