import json
import time

from collections import deque

#use numpy

'''
records population and district for each VTD 

@param d: dictionary name
@param popId: key for population value
@param districtId: key for district value

@return dictionary 
'''
def countEntries(d, popId, districtId):

    table = {}

    counter = 0

    for key in d['nodes']:
        table[counter] = {}
        table[counter]['district'] = key[districtId]
        table[counter]['population'] = key[popId]
        counter += 1

    return table


'''
converts json to matrix

@param table: table name

@return a matrix
'''
def dictToMatrix(table):
    sum = 0
    matrix = []
    for i in range(len(table)):
        matrix.append([])
        for j in range(len(table)):
            matrix[i].append(0)
    
    for key1 in table:
        for key2 in table:
            if key1 == key2:
                continue
            elif table[key1]['district'] == table[key2]['district']:
                #matrix[key1][key2] = 1
                pop1 = table[key1]['population']
                pop2 = table[key2]['population']
                totalPop = pop1 * pop2
                sum += totalPop
                matrix[key1][key2] = totalPop
    print(sum)

    return matrix

'''
computes pair distance for matrix A and centroid (A_c)

@param a1: matrix
@param centroid: the centroid map
@param distance: (boolean) whether to return the distance or not

@return either the updated centroid map or the distance
'''
def pairDistance(a1, centroid, distance):
    sum = 0
    for i in range(len(a1)):
        for row in range(len(a1)-i):
            col = i + row

            value1 = centroid[row][col]
            value2 = a1[row][col]

            if distance:
                sum += abs(value1-value2)

            else:
                centroid[row][col] = abs(value1+value2)
    
    if distance:
        return distance / 2

    else:
        return centroid

# END FUNCTIONS #

start = time.time()

numGraphs = 10

centroid = []
for i in range(10000):
    centroid.append([])
    for j in range(10000):
        centroid[i].append(0)


districtId = '2011_PLA_1'
popId = 'TOT_POP'

stack = deque()

#calculates centroid map
for i in range(1, numGraphs+1): #since I labeled the json files using 1 indexing

    fdir = "./JSON_Files/plot" + str(i) + ".json"
    with open(fdir) as a:
        dict1 = json.load(a)

    res = countEntries(dict1, popId = popId, districtId = districtId)

    matrix = dictToMatrix(res)

    stack.append(matrix)
    
    centroid = pairDistance(matrix, centroid, False)

    if i % 10 == 0 or i == 1:
        print("Graph " + str(i) + " done")

#divides each entry in the final centroid map by T
sum1 = 0
sum2 = 0
for i in range(len(centroid)):
    for j in range(len(centroid[i])):
        sum1 += centroid[i][j]
        centroid[i][j] /= numGraphs 
        sum2 += centroid[i][j]

currTime = time.time()
print("Centroid calculated")
print("Time elapsed so far: " + str((currTime-start) // 60) + "minutes")

minDiff = float('inf')

i = numGraphs #pops each element so start counting from the end

distances = []

while len(stack) != 0:
    matrix = stack.pop() #rightmost element
    distance = pairDistance(matrix, centroid, True)

    distances.append((distance), i)
    
    if distance < minDiff:
        minDiff = distance
        minMapNum = i

    if i % 10 == 0:
        print("Graph " + str(i) + " analyzed")

    i -= 1

end = time.time()
print("Done")
timeElapsed = (end - start) // 60 #in minutes
print("Took " + str(timeElapsed) + " minutes")
print("Distances array: ")
print(distances)

print("Minimum distance " + str(minDiff))
print("Map chosen" + str(minMapNum))
