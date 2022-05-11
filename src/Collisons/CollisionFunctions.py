from src.Utility.EuclidianFunctions import pointToLineDistance, pointToSegmentDistance

# TODO: Transfer all main collision functions here

pointLineEpsilon = 4


def ifPolygonCollidesWithRound(polygonCollisonModel, roundCollisionModel):
    minDistance = float('inf')
    listLen = len(polygonCollisonModel.pointList)
    for i in range(listLen):
        pld = pointToSegmentDistance([polygonCollisonModel.pointList[i % listLen], polygonCollisonModel.pointList[(i + 1) % listLen]],
                                  roundCollisionModel.getPoint())
        minDistance = min(pld, minDistance)
    return minDistance < pointLineEpsilon + roundCollisionModel.r


def whichSurfaceOfPolygonCollidesWithRound(polygonCollisonModel, roundCollisionModel):  # TODO: Make one function with the one above
    minDistance = float('inf')
    listLen = len(polygonCollisonModel.pointList)
    for i in range(listLen):
        pld = pointToSegmentDistance(
            [polygonCollisonModel.pointList[i % listLen], polygonCollisonModel.pointList[(i + 1) % listLen]],
            roundCollisionModel.getPoint())
        minDistance = min(pld, minDistance)
        if minDistance < pointLineEpsilon + roundCollisionModel.r:
            return [polygonCollisonModel.pointList[i % listLen], polygonCollisonModel.pointList[(i + 1) % listLen]]
    return None


def ifPointCollidesWithLine(point, line):
    return pointToSegmentDistance(line, point) < pointLineEpsilon
