#!/usr/bin/python
import os
import sys
import functions as func

from city import City
from argparse import ArgumentParser      

#*******************************************************************************************************************************************************
# Uses ArgumentParser to get the command line arguments
#*******************************************************************************************************************************************************
parser = ArgumentParser(description = 'Implements the A* algorithm on an arbitrary map described through a "connections" file and a "location" file.')

parser.add_argument('-c', dest = 'connections', help = 'Specify path to the connections.txt file.', type = lambda f: func.is_valid_file(parser, f), required = True, metavar = "FILE")
parser.add_argument('-l', dest = 'locations', help = 'Specify path to the locations.txt file.', type = lambda f: func.is_valid_file(parser, f), required = True, metavar = "FILE")
parser.add_argument('-s', dest = 'start', help = 'Specify the city to start in.', type = str)
parser.add_argument('-e', dest = 'end', help = 'Specify the city to end in.', type = str)
parser.add_argument('-x', dest = 'exclude', help = 'Specifiy the city(cities) to exclude, separated with a comma.', type = lambda s: [int(i) for i in s.split(',')])
parser.add_argument('-H', dest = 'heuristic', help = 'Specify the heuristic to use: 0 - Straight line (Default), 1 - Fewest links.', nargs = '?', const = 0, type = int, default = 0)
parser.add_argument('--option', dest = 'option', help = 'Specify how to show steps: 0 - Full optimal path (Default), 1 - Step-by-step (Enter key)', nargs = '?', const = 0, type = int,default = 0)

args = parser.parse_args()
#*******************************************************************************************************************************************************

if __name__ == '__main__':

    loc_f = args.locations.readlines()
    con_f = args.connections.readlines()

    args.locations.close()
    args.connections.close()

    # Get the map of the cities
    cityMap = func.getCities(loc_f, con_f)
    print 'Cities obtained'

    # If heuristic is straight line
    if args.heuristic == 0:
        Staight_Line(args.start, args.end)
    
    # If heuristic is fewest links
    else:
        Fewest_Links(args.start, args.end)