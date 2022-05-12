from src.Utility.EuclidianFunctions import pointToLineDistance, pointToSegmentDistance, pointToPointDistance, \
    surfaceContainsPointShadow

# TODO: Transfer all main collision functions here

pointLineEpsilon = 4


def surfaceOfPolygonRoundCollision(polygonCollisonModel, roundCollisionModel):
    listLen = len(polygonCollisonModel.pointList)
    for i in range(listLen):
        testedSegment = [polygonCollisonModel.pointList[i % listLen], polygonCollisonModel.pointList[(i + 1) % listLen]]
        if surfaceContainsPointShadow(testedSegment, roundCollisionModel.getPoint()):
            pld = pointToSegmentDistance(testedSegment, roundCollisionModel.getPoint())
            if pld < pointLineEpsilon + roundCollisionModel.r:
                return testedSegment
    return None


def ifPointCollidesWithLine(point, line):
    return pointToSegmentDistance(line, point) < pointLineEpsilon


def ifRoundCollidesWithRound(r1, r2):
    return pointToPointDistance(r1.getPoint(), r2.getPoint()) < r1.r + r2.r
