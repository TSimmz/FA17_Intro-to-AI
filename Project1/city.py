import math

#*****************************************************
# City class to hold the coordinates of the city, the
#   connections, and the distance btwn connections
#*****************************************************
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

    def __repr__(self):
        return str(self)
        
    def __str__(self):
        return self.name

    def setParent(self, p):
        self.parent = p

    def setStart(self):
        self.start = True
    
    def setEnd(self):
        self.end = True

    def setCost(self, f):
        self.cost = f

    def addConnection(self, conn):
        self.connections.append(conn)

    def calculateDistance(self, city):
        return math.sqrt(pow(self.x-city.x, 2) + pow(self.y-city.y, 2))

    def getConnectionDists(self):
        for city in self.connections:
            dist = self.calculateDistance(city)
            self.connDist.append(dist)
    
    def getCityCount(self):
        return self.cityCount

    
