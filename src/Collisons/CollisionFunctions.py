from src.Utility.EuclidianFunctions import pointToLineDistance, pointToSegmentDistance

# TODO: Transfer all main collision functions here

pointLineEpsilon = 2


def ifPolygonCollidesWithRound(polygonCollisonModel, roundCollisionModel):  # TODO: test
    minDistance = float('inf')
    for i in range(len(polygonCollisonModel.pointList)):
        pld = pointToLineDistance([polygonCollisonModel.pointList[i], polygonCollisonModel.pointList[i + 1]],
                                  roundCollisionModel.getPoint())
        minDistance = min(pld, minDistance)
    return minDistance < pointLineEpsilon


def ifPointCollidesWithLine(point, line):
    return pointToSegmentDistance(line, point) < pointLineEpsilon
