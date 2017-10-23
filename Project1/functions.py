#***************************************************************************
#***************************************************************************
# Functions.py contains all necessary helper functions for the main.py file
#***************************************************************************
#***************************************************************************
import os
import sys
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
# Performs a basic heuristic score from start to finish
#*********************************************************************
# def Estimate_Score(start, end):
#     return None

#*********************************************************************
# Function to perform the straight-line heuristic
#*********************************************************************
# def Straight_Line(start, end, cityMap):
#     vestibule = [start]
#     processed = []
#     prevPath = dict()
    
#     sScore = dict()
#     sScore[start] = 0
    
#     eScore = dict()
#     eScore[start] = Estimate_Score(start, end)

#     while vestibule:
#         temp = sScore.values
#         cur = temp.min
#         if cur == end:
#             return Final_Path(prevPath, cur)
        
#         vestibule.remove(cur)
#         processed.append(cur)

#         for n in cur.connections:
#             if n in processed:
#                 continue

#             if n not in vestibule:
#                 vestibule.append(n)

#             temp_score = sScore[cur] + cur.calculateDistance(n)
#             if temp_score >= sScore[n]
#                 continue

#             prevPath[n] = cur
#             sScore[n] = temp_score
#             eScore[n] = sScore[n] + Estimate_Score(cur, end)
        
#         return False

#*********************************************************************
# Returns the final path to the problem
#*********************************************************************
# def FinalPath(prevPath, current):
#     return None
    