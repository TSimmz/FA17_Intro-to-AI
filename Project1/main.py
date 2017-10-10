#!/usr/bin/python
import os
import sys
import functions

from city import City
from argparse import ArgumentParser      

#*******************************************************************************************************************************************************
# Uses ArgumentParser to get the command line arguments
#*******************************************************************************************************************************************************
parser = ArgumentParser(description = 'Implements the A* algorithm on an arbitrary map described through a "connections" file and a "location" file.')
parser.add_argument('-c', dest = 'connections', help = 'Specify path to the connections.txt file.', 
    type = lambda f: is_valid_file(parser, f), required = True, metavar = "FILE")
parser.add_argument('-l', dest = 'locations', help = 'Specify path to the locations.txt file.', type = lambda f: is_valid_file(parser, f), metavar = "FILE")
parser.add_argument('-s', dest = 'start', help = 'Specify the city to start in.', type = str)
parser.add_argument('-e', dest = 'end', help = 'Specify the city to end in.', type = str)
parser.add_argument('-x', dest = 'exclude', help = 'Specifiy the city(cities) to exclude, separated with a comma.', type = lambda s: [int(i) for i in s.split(',')])
parser.add_argument('-H', dest = 'heuristic', help = 'Specify the heuristic to use: 0 - Straight line (Default), 1 - Fewest links.',
    nargs = '?', const = 0, type = int, default = 0)
parser.add_argument('--option', dest = 'option', help = 'Specify how to show steps: 0 - Full optimal path (Default), 1 - Step-by-step (Enter key)',
    nargs = '?', const = 0, type = int,default = 0)
args = parser.parse_args()
#*******************************************************************************************************************************************************


if __name__ == '__main__':
    loc_start = args.start
    loc_end = args.end
    exclude = args.exclude
    heuristic = args.heuristic
    option = args.option

    with open(args.locations) as loc_f:
        loc = loc_f.readlines()
        loc_f.close()

    with open(args.connections) as con_f:
        con = con_f.readlines()
        con_f.close()

    cityMap = getCities(loc, con)        
    print 'Cities obtained'
    
    #if args.heuristic == 0:
    #    Staight_Line(loc_start, loc_end)