# Centralized Fairness

**chain.py**

This runs the Markov chain for 10,000 steps. Every 100 steps, it will save the partition to a JSON file, located in ./JSON_Files/. They are enumerated from 1 to n, where n is the nth JSON file to be saved (in other words, # of steps in chain // 100)

**centralized.py**

This file calculates the centroid map and finds a map A* whose distance is minimized with respect to the centroid map. It iterates through the JSON files saved previously in chain.py, and first outputs a matrix where point (i , j) = (population of entry i * population of entry j) if entry i and entry j are within the same district. Then it calculates the pair distance and updates the centroid. Lastly, it utilizes the deque module (reference: https://docs.python.org/3/library/collections.html) to add each matrix to a stack to be used later to find the matrix closest to the centroid. 

After finding the centroid, it pops each matrix off of the stack and calculates the pair distance, updating the minimum distance accordingly. 

**Helpful Links for Using Gerrychain**

GerryChain docs: https://gerrychain.readthedocs.io/en/latest/index.html

Guide to GerryChain by D. Deford: http://www.math.wsu.edu/faculty/ddeford/GerryChain_Guide.pdf

Examples using GerryChain: https://github.com/drdeford/GerryChain-Templates

