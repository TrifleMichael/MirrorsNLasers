import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def apply2dRotation(vec, angle):
    return [vec[0] * math.cos(angle) - vec[1] * math.sin(angle),
            vec[0] * math.sin(angle) + vec[1] * math.cos(angle)]


def rotate2dLine(p1, p2, rotationP, angle):
    """Rotates line from p1 to p2 around rotationP by the given angle"""

    # Translating to coordinate system that begins at rotationP
    start = (p1[0] - rotationP[0], p1[1] - rotationP[1])
    end = (p2[0] - rotationP[0], p2[1] - rotationP[1])

    start = apply2dRotation(start, angle)
    end = apply2dRotation(end, angle)

    start = (start[0] + rotationP[0], start[1] + rotationP[1])
    end = (end[0] + rotationP[0], end[1] + rotationP[1])
    return start, end


def lineAngle(p1, p2):
    """Angle in relation to up direction, counted clockwise"""
    return -(math.atan2(p2[0] - p1[0], p2[1] - p1[1])) % (2 * math.pi)


def bounceVector(vec, p1, p2):
    """Reflects vector of a surface defined by two points"""
    surfaceAngle = lineAngle(p1, p2)
    vec = apply2dRotation(vec, -surfaceAngle)
    vec[0] *= -1
    vec = apply2dRotation(vec, surfaceAngle)
    return vec


def pointToLineDistance(line, point):
    start = line[0]
    end = line[1]
    angle = -lineAngle(start, end)

    point = apply2dRotation(point, angle)
    start, end = rotate2dLine(start, end, [0, 0], angle)

    # TODO: detect if point cast is beyond mirrors edges
    # TODO: fix weird angle calculations
    return abs(point[0] - start[0])


def surfaceContainsPointShadow(surface, point):
    """Checks if the shadow cast perpendicular to the surface lands on it"""
    pass


def pointToPointDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
