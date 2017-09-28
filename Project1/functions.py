#***************************************************************************
#***************************************************************************
# Functions.py contains all necessary helper functions for the main.py file
#***************************************************************************
#***************************************************************************

from argparse import ArgumentParser

#*********************************************************************
# Used in the lambda function for parser
#  Checks to see if the file is valid
#  Opens the file if valid, throws error if invalid
#*********************************************************************
def is_valid_file(parser, file):
    if os.path.exists(file):
        return
    else:
        parser.error("The file %s does not exist." % file)

#*********************************************************************
# Gets the list of cities with all data from input files
#*********************************************************************
def getCities(locations, connections):
    cities = []

    for line in locations:
        if line == "END":
            break

        line.split()
        c = City(line[0], line[1], line[2])
        cities.append(c)

    for line in connections:
        if line == "END":
            break
        
        line.split()
        #for c in cities:
        #    if line[0] == c.name:
                
    return cities

#*********************************************************************
# Performs a basic heuristic score from start to finish
#*********************************************************************
def Estimate_Score(start, end):
    return None
#*********************************************************************
# Function to perform the straight-line heuristic
#*********************************************************************
def Straight_Line(start, end, cityMap):
    vestibule = [start]
    processed = []
    prevPath = dict()
    
    sScore = dict()
    sScore[start] = 0
    
    eScore = dict()
    eScore[start] = Estimate_Score(start, end)

    while vestibule:
        temp = sScore.values
        cur = temp.min
        if cur == end:
            return Final_Path(prevPath, cur)
        
        vestibule.remove(cur)
        processed.append(cur)

        for n in cur.connections:
            if n in processed:
                continue

            if n not in vestibule:
                vestibule.append(n)

            temp_score = sScore[cur] + cur.calculateDistance(n)
            if temp_score >= sScore[n]
                continue

            prevPath[n] = cur
            sScore[n] = temp_score
            eScore[n] = sScore[n] + Estimate_Score(cur, end)
        
        return False

#*********************************************************************
# Returns the final path to the problem
#*********************************************************************
def FinalPath(prevPath, current):
    return None
    