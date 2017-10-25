#***************************************************************************
#***************************************************************************
# Class: City
# Function: Stores information about each city
#***************************************************************************
#***************************************************************************
import math

class City():
    cityCount = 0
    
    # City constructor
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.start = False
        self.end = False
        self.cost = float("inf")
        self.connections = []
        self.connDist = []
        City.cityCount += 1
    
    # City destructor
    def __del__(self):
        class_name = self.__class__.__name__
        #print class_name, "destroyed."

    # Used to represent object as string
    def __repr__(self):
        return str(self)

    # Similar to ToString() method
    def __str__(self):
        return self.name

    # Sets the parent of city
    def setParent(self, p):
        self.parent = p

    # Sets start member if city is start
    def setStart(self):
        self.start = True
    
    # Sets end member if city is end
    def setEnd(self):
        self.end = True

    # Sets cost if using straight-line
    def setCost(self, f):
        self.cost = f

    # Adds a city to the list of connections
    def addConnection(self, conn):
        self.connections.append(conn)

    # Calculates the distance between two cities
    def calculateDistance(self, city):
        return math.sqrt(pow(self.x-city.x, 2) + pow(self.y-city.y, 2))

    # Gets the distances of each cities connected cities
    def getConnectionDists(self):
        for city in self.connections:
            dist = self.calculateDistance(city)
            self.connDist.append(dist)
    
    # Returns count of cities
    def getCityCount(self):
        return City.cityCount

    
