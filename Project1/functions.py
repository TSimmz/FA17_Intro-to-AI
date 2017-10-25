#***************************************************************************
#***************************************************************************
# Functions.py contains all necessary helper functions for the main.py file
#***************************************************************************
#***************************************************************************
import os
import sys
import math

from city import City
from queue import Queue
from argparse import ArgumentParser

#*********************************************************************
# Used in the lambda function for parser
#  Checks to see if the file is valid
#  Opens the file if valid, throws error if invalid
#*********************************************************************
def is_valid_file(parser, file):
    if os.path.exists(file):
        return open(file, 'r')
    else:
        parser.error("The file %s does not exist." % file)

#*********************************************************************
# Gets the list of cities with all data from input files
#*********************************************************************
def getCities(locations, connections):
    cities = []
    
    # Get all cities and X/Y coordinates
    for line in locations:
        if line == "END":
            break
        
        l = line.split()
        c = City(l[0], int(l[1]), int(l[2]))

        cities.append(c)
    
    # Get city connections
    for line in connections:
        if line == "END":
            break

        l = line.split()

        for c in cities:
            if c.name == l[0]:
                for n in range(1, int(l[1]) + 1):
                    for d in cities:
                        if d.name == l[1+n]:
                            c.addConnection(d)

    # Calculate distances for each city's connected cities
    for city in cities:
        city.getConnectionDists()
                
    return cities

#*********************************************************************
# Removed cities if excluded cities parameter was entered
#*********************************************************************
def RemoveCities(cityMap, ex):
    for e in ex:
        for c in cityMap:
            if e == c.name:
                cityMap.remove(c)
                print c.name, "removed."

#*********************************************************************
# Performs a basic heuristic score from start to finish
#*********************************************************************
def Estimate_Cost(start, end):
    return math.floor(start.calculateDistance(end))

#*********************************************************************
# Finds the minimum cost in the openedList
#*********************************************************************
def FindMinimum(op):
    minCost = []
    for city in op:     # Get list of costs in openedList
        minCost.append(city.cost)
    
    for city in op:     # Gets city with minimum cost
        if min(minCost) == city.cost:
            q = city

    return q

#*********************************************************************
# Function to perform the straight-line heuristic
#*********************************************************************
def SL_Heuristic(cityMap, start, end, opt):
    openedList = []     # List to be checked cities
    closedList = []     # List of already check cities
    tempCity = start    # Temporary City for returnPath
    done = False

    f = dict()          # Dictionary for overall cost
    g = dict()          # Dictionary for calculated cost
    h = dict()          # Dictionary for estimated cost

    distance = 0        # Current distance
    returnPath = dict() # Dictionary for return path

    openedList.append(start)    # Add start city to openedList
    f[start.name] = 0           # Initialize start cost to 0
    g[start.name] = 0           # Initialize start cost to 0
    h[start.name] = start.calculateDistance(end) # Estimate start to distance to goal

    # Loop while cities are in OpenedList
    while openedList:
        
        q = FindMinimum(openedList)         # Find city in openedList with minimum overall cost
        returnPath[tempCity.name] = q.name  # Set current city's parent city

        distance = distance + tempCity.calculateDistance(q) # Update distance

        if opt == 1:
            print 'Current Path:', closedList
            print 'Distance Traveled: %.2f' % distance
            print 'Best move is to: ', q.name
            
        if done == True:
            closedList.append(q)
            print '\nFinal Path:', closedList, '\n'
            return

        # Remove q from the openedList
        for c in openedList:
            if c.name == q.name:
                openedList.remove(c)

        # Check all connected neighbors of q
        for n in q.connections:

            # Check to see if we've reached the end
            if n.name == end.name:
                done = True        

            # Calculate costs and heuristic estimate
            g[n.name] = g[q.name] + q.calculateDistance(n)
            h[n.name] = Estimate_Cost(n, end)
            f[n.name] = g.get(n.name) + h.get(n.name)

            # Set overall cost for city
            n.cost = f.get(n.name)

            # If neighbor is in openedList and new cost is less, update
            if n in openedList:
                for city in cityMap:
                    if city.name == n.name and city.cost > n.cost:
                        city.setCost(f.get(n.name))
                        break

            # If neighbor is in closedList and new cost is less, update    
            if n in closedList:
                for city in cityMap:
                    if city.name == n.name and city.cost > n.cost:
                        city.setCost(f.get(n.name))
                        break

            # Else add neighbor to openedList
            else:
                openedList.append(n)
        
        # Add current city to closedList
        closedList.append(q)
        tempCity = q

        # If step-by-step
        if opt == 1:
            cont = raw_input()
            if cont == '':
                continue
    
    print 'Path not found!'
    return

#*********************************************************************
# Returns the final path to the problem
#*********************************************************************
def FinalPath(state, returnPath, cityMap):
    print 'Optimal Path:'
    path = []
    path.append(state.name)

    while True:
        p = returnPath.get(state.name)
        if CheckStartCity(cityMap, state) == True:
            break
        else:
            path.append(p)
            state = FindCityByName(cityMap, p)

    path.reverse()
    d = len(path) - 1

    print path
    print 'Distance Traveled:', d

#*********************************************************************
# Returns the city from the cityMap from passed city
#*********************************************************************
def FindCity(cityMap, find):
    for city in cityMap:
        if city.name == find.name:
            return city

#*********************************************************************
# Returns the city from the cityMap from passed city name
#*********************************************************************
def FindCityByName(cityMap, find):
    for city in cityMap:
        if city.name == find:
            return city

#*********************************************************************
# Checks to see if city is starting city
#*********************************************************************
def CheckStartCity(cityMap, find):
    for city in cityMap:
        if city.name == find.name and find.start == True:
            return True

#*********************************************************************
# Function to perform the fewest links heuristic
#*********************************************************************
def FL_Heuristic(cityMap, start, end, opt):
    q = Queue()
    q.enqueue(FindCity(cityMap, start))

    visited = []

    returnPath = dict()
    returnPath[start.name] = (None)

    while not q.isEmpty():
        current = FindCity(cityMap, q.dequeue())

        if current.name == end.name:
                print 'Final ',
                FinalPath(current, returnPath, cityMap)
                return

        for n in current.connections:
            
            if n.name in visited:
                continue

            qList = q.getList()

            if n not in qList:
                returnPath[n.name] = current.name
                q.enqueue(n)

            if opt == 1:
                FinalPath(n, returnPath, cityMap)
                print '\n'

        visited.append(n.name)

        if opt == 1:
            cont = raw_input()
            if cont == '':
                continue

    print 'Path not found!'
    return