import json

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
    seenKeys = set()
    matrix = []
    for i in range(len(table)):
        matrix.append([])
        for j in range(len(table)):
            matrix[i].append(0)
    
    for key1 in table:
        for key2 in table:
            if key1 == key2:
                continue
            elif (key2, key1) in seenKeys:
                continue
            elif table[key1]['district'] == table[key2]['district']:
                pop1 = table[key1]['population']
                pop2 = table[key2]['population']
                totalPop = pop1 * pop2
                seenKeys.add((key1, key2))
                matrix[key1][key2] = totalPop

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
            centroid[row][col] += abs(value1-value2)
            if distance:
                sum += abs(value1-value2)
    
    if distance:
        return distance / 2

    else:
        return centroid

# END FUNCTIONS #

numGraphs = 101

centroid = []
for i in range(10000):
    centroid.append([])
    for j in range(10000):
        centroid[i].append(0)


districtId = '2011_PLA_1'
popId = 'TOT_POP'

#calculates centroid map
for i in range(numGraphs)

    fdir = "./JSON_Files/plot" + str(i) + ".json"
    with open(fdir) as a:
        dict1 = json.load(a)

    res = countEntries(dict1, popId = popId, districtId = districtId)

    matrix = dictToMatrix(res)
    
    centroid = pairDistance(matrix, centroid, False)

    print("Graph " + str(i) + " done")

#divides each entry in the final centroid map by T
for i in range(len(centroid)):
    for j in range(len(centroid[i])):
        centroid[i][j] /= numGraphs 

print("Centroid calculated")

minDiff = float('inf')

for i in range(numGraphs): #should i just reopen every json file and do this again? 

    fdir = "./JSON_Files/plot" + str(i) + ".json"

    with open(fdir) as a:
        dict1 = json.load(a)

    res = countEntries(dict1, popId = popId, districtId = districtId)
    matrix = dictToMatrix(res)
    
    distance = pairDistance(matrix, centroid, True)
    
    if distance < minDiff:
        minDiff = distance
        minMap = matrix

    print("Graph + " + str(i) + " analyzed")

print("Done")

print(minMap)
print(minDiff)

