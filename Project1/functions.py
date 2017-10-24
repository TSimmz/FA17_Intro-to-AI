#***************************************************************************
#***************************************************************************
# Functions.py contains all necessary helper functions for the main.py file
#***************************************************************************
#***************************************************************************
import os
import sys
import math
from city import City
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
    for city in op:     # Get list if costs in openedList
        minCost.append(city.cost)
    
    for city in op:
        if min(minCost) == city.cost:
            q = city

    return q

#*********************************************************************
# Function to perform the straight-line heuristic
#*********************************************************************
def Straight_Line2(start, end, cityMap, opt):
    openedList = []     # List to be checked cities
    closedList = []     # List of already check cities
    tempCity = start    # TemporaryCity for returnPath

    f = dict()          # Dictionary for overall cost
    g = dict()          # Dictionary for calculated cost
    h = dict()          # Dictionary for estimated cost

    distance = 0        # Current distance
    returnPath = dict() # Dictionary for return path
    returnPath[start.name] = '' # Initializing start key to empty string

    openedList.append(start) # Add start city to openedList
    f[start.name] = 0   # Initialize start cost to 0
    g[start.name] = 0   # Initialize start cost to 0
    h[start.name] = start.calculateDistance(end) # Estimate start to distance to goal

    # Loop while cities are in OpenedList
    while openedList:
        
        q = FindMinimum(openedList)         # Find city in openedList with minimum overall cost
        returnPath[q.name] = tempCity.name  # Set current city's parent city

        if opt == 1:
            print 'Current Path:', closedList
            print 'Distance Traveled:',  distance
            print 'Best move is to: ', q.name

        #print 'Current city is', q.name,'\n'        

        # Remove q from the openedList
        for c in openedList:
            if c.name == q.name:
                openedList.remove(c)

        # Check all connected neighbors of q
        for n in q.connections:

            # Check to see if we've reached the end
            if n.name == end.name:
                
                if opt == 0:
                    print 'Optimal Path:'

                return         

            # Calculate costs and heuristic estimate
            g[n.name] = g[q.name] + q.calculateDistance(n)
            h[n.name] = Estimate_Cost(n, end)
            f[n.name] = g.get(n.name) + h.get(n.name)

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
                
        if opt == 1:
            cont = raw_input()
            if cont == '':
                continue

#*********************************************************************
# Returns the final path to the problem
#*********************************************************************
def FinalPath(prevPath, current):
    return None

#*********************************************************************
# Function to perform the fewest links heuristic
#*********************************************************************
def Fewest_Links(start, end, cityMap, opt):
    return None    