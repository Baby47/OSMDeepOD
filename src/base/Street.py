from geopy import Point
from geopy.distance import vincenty
import numpy as np

class Street:
    def __init__(self):
        self.nodes = []
        self.name = ""
        self.ident = 0
        self.highway = "-"

    def getLeftNode(self):
        if(self.nodes[0].lon < self.nodes[1].lon):
            return self.nodes[0]
        else:
            return self.nodes[1]

    def getRightNode(self):
        if(self.nodes[0].lon > self.nodes[1].lon):
            return self.nodes[0]
        else:
            return self.nodes[1]

    def getAngle(self):
        zero = Point(0,0)
        left = self.getLeftNode()
        right = self.getRightNode()
        latDiff = right.lat - left.lat
        lonDiff = right.lon - left.lon
        latPoint =  Point(latDiff, 0)
        lonPoint = Point(0, lonDiff)

        verticalDistance = vincenty(zero, latPoint).meters
        horizontalDistance = vincenty(zero, lonPoint).meters

        angle = np.arctan(verticalDistance/horizontalDistance)
        if(latDiff<0): angle *= -1
        return angle





