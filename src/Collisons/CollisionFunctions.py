from src.Utility.EuclidianFunctions import pointToLineDistance

# TODO: Transfer all main collision functions here

pointLineEpsilon = 2


def ifPolygonCollidesWithRound(self, polygonCollisonModel, roundCollisionModel):
    minDistance = float('inf')
    for i in range(len(self.pointList)):
        pld = pointToLineDistance([polygonCollisonModel.pointList[i], polygonCollisonModel.pointList[i + 1]],
                                  roundCollisionModel.getPoint())
        minDistance = min(pld, minDistance)
    return minDistance < pointLineEpsilon

