#!/usr/bin/python
import os
import sys
import time
import functions as func

from city import City
from argparse import ArgumentParser      

#*******************************************************************************************************************************************************
# Uses ArgumentParser to get the command line arguments
#*******************************************************************************************************************************************************
parser = ArgumentParser(description = 'Implements the A* algorithm on an arbitrary map described through a "connections" file and a "location" file.')

parser.add_argument('-c', dest = 'connections', help = 'Specify path to the connections.txt file.', type = lambda f: func.is_valid_file(parser, f), required = True, metavar = "FILE")
parser.add_argument('-l', dest = 'locations', help = 'Specify path to the locations.txt file.', type = lambda f: func.is_valid_file(parser, f), required = True, metavar = "FILE")
parser.add_argument('-s', dest = 'start', help = 'Specify the city to start in.', required = True, type = str)
parser.add_argument('-e', dest = 'end', help = 'Specify the city to end in.', required = True, type = str)
parser.add_argument('-x', dest = 'exclude', help = 'Specifiy the city(cities) to exclude, separated with a comma.', type = lambda s: [str(i) for i in s.split(",")])
parser.add_argument('-H', dest = 'heuristic', help = 'Specify the heuristic to use: 0 - Straight line (Default), 1 - Fewest links.', nargs = '?', const = 0, type = int, default = 0)
parser.add_argument('--option', dest = 'option', help = 'Specify how to show steps: 0 - Full optimal path (Default), 1 - Step-by-step (Enter key)', nargs = '?', const = 0, type = int,default = 0)

args = parser.parse_args()
#*******************************************************************************************************************************************************

if __name__ == '__main__':
    # Starts taking the time
    s = time.time()

    # Get the data from the open files
    loc_f = args.locations.readlines()
    con_f = args.connections.readlines()

    # Close the open files
    args.locations.close()
    args.connections.close()

    #*********************************************************************
    # Get the map of the cities
    #*********************************************************************
    cityMap = func.getCities(loc_f, con_f)
    print '\nCities obtained'

    #*********************************************************************
    # Remove cities if excluded
    #*********************************************************************
    if args.exclude != None:
        func.RemoveCities(cityMap, args.exclude)
    else:
        print 'No cities to exclude.'

    #*********************************************************************
    # Set start and end cities
    #*********************************************************************
    start = None
    end = None

    for city in cityMap:
        if city.name == args.start:
            city.setStart()
            start = city
            print city.name, "set as Start."
        
        if city.name == args.end:
            city.setEnd()
            end = city
            print city.name, "set as End."

    # Start and end city validation
    if start == None:
        print 'Invalid Start city...\tExiting.\n'
        exit()
    if end == None:
        print 'Invalid End city...\tExiting.\n'
        exit()

    #*********************************************************************
    # Full path or step-by-step
    #*********************************************************************
    if args.option == 0:
        print 'Printing full path.'
    else:
        print 'Printing step-by-step. Press enter to move.'

    #*********************************************************************
    # Heuristic choice from command line argument
    #*********************************************************************
    if args.heuristic == 0:
        print 'Using Straight-Line heuristic.\n\n'
        func.SL_Heuristic(cityMap, start, end, args.option)
    else:
        print 'Using Fewest-Links heuristic.\n\n'
        func.FL_Heuristic(cityMap, start, end, args.option)

    # Takes finish time and prints total time
    e = time.time()
    total = e - s
    print 'Total Time Elapsed: %.5f seconds' % total

    