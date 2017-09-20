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
        self.connections = []
        self.connDist = []
        City.cityCount += 1
    
    # City destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed."

    def addConnection(self, conn):
        self.connections.append(conn)

    def calculateDistance(self, city):
        return math.sqrt(math.pow(self.x-city.x, 2) + math.pow(self.y-city.y, 2))

    def getConnectionDists(self):
        for city in self.connections:
            dist = calculateDistance(city)
            self.connDist.append(dist)
    
    def getCityCount(self):
        return self.cityCount

    
