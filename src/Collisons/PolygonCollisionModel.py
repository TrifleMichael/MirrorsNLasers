from src.Utility.EuclidianFunctions import pointToLineDistance


class PolygonCollisionModel:
    def __init__(self, pointList):
        # Assumes the last point in list connects with first
        self.pointList = pointList