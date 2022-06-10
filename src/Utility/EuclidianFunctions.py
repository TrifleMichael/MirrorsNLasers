import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def pointToPointDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def apply2dRotation(vec, angle):
    """Clockwise rotation"""
    return [vec[0] * math.cos(angle) - vec[1] * math.sin(angle),
            vec[0] * math.sin(angle) + vec[1] * math.cos(angle)]


def rotate2dLine(p1, p2, rotationP, angle):
    """Rotates line from p1 to p2 around rotationP by the given angle clockwise"""

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
    return -(math.atan2(p2[0] - p1[0], p2[1] - p1[1]) - math.pi) % (2 * math.pi)


def bounceVector(vec, p1, p2, dampening=0):
    """Reflects vector of a surface defined by two points"""
    surfaceAngle = lineAngle(p1, p2)
    vec = apply2dRotation(vec, -surfaceAngle)
    vec[0] *= -1 * (1 - dampening)
    vec = apply2dRotation(vec, surfaceAngle)
    return vec


def pointToLineDistance(line, point):  # TODO: Name does not match order of arguments
    """Distance from point to infinite line defined by two points"""
    start = line[0]
    end = line[1]
    angle = -lineAngle(start, end)

    point = apply2dRotation(point, angle)
    start, end = rotate2dLine(start, end, [0, 0], angle)

    return abs(point[0] - start[0])


def surfaceContainsPointShadow(surface, point):
    """Checks if the shadow of point cast perpendicular to the surface lands on it"""
    surfaceAngle = -lineAngle(surface[0], surface[1])
    rotatedPoint = apply2dRotation(point, surfaceAngle)
    rotatedSurface = rotate2dLine(surface[0], surface[1], [0, 0], surfaceAngle)
    return rotatedSurface[0][1] <= rotatedPoint[1] <= rotatedSurface[1][1] \
           or rotatedSurface[1][1] <= rotatedPoint[1] <= rotatedSurface[0][1]


def pointToSegmentDistance(segment, point):
    """Distance from point to segment defined by two points"""
    start = segment[0]
    end = segment[1]
    angle = -lineAngle(start, end)

    rPoint = apply2dRotation(point, angle)
    start, end = rotate2dLine(start, end, [0, 0], angle)

    if surfaceContainsPointShadow((start, end), rPoint):
        return abs(rPoint[0] - start[0])
    else:
        return min(pointToPointDistance(start, rPoint),
                   pointToPointDistance(end, rPoint))


def lineTangentToPoints(p1, p2):
    m = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    rAng = lineAngle(m, p2)
    line = [[0, 0], [1, 0]]
    return rotate2dLine(line[0], line[1], [0, 0], rAng)


def movePointAwayFromSurface(point, surface, distance):
    ang = lineAngle(surface[0], surface[1])
    l, r = rotate2dLine(surface[0], surface[1], [0, 0], ang)
    p = apply2dRotation(point, ang)
    if p[0] < l[0]:
        p[0] -= distance
    else:
        p[0] += distance

    p = apply2dRotation(p, -ang)
    return p


def shiftLineToPoint(line, point):
    xShift = point[0] - line[0][0]
    yShift = point[1] - line[0][1]
    return [[line[0][0] + xShift, line[0][1] + yShift], [line[1][0] + xShift, line[1][1] + yShift]]


def movePointAwayFromPoint(point, repulsingPoint, distance):
    vec = [point[0] - repulsingPoint[0], point[1] - repulsingPoint[1]]
    if vec == [0, 0]:
        return point[:]
    vecLen = pointToPointDistance(vec, [0, 0])
    vec = [vec[0] * distance / vecLen, vec[1] * distance / vecLen]
    return [point[0] + vec[0], point[1] + vec[1]]


def pointsNormalVector(p1, p2):
    """Returns a vector of length 1 pointing from p1 to p2"""
    dist = pointToPointDistance(p1, p2)
    return (p2[0] - p1[0]) / dist, (p2[1] - p1[1]) / dist


# print(movePointAwayFromSurface([0.5, 0.5], [[0, 0], [1, 1]], 1))

def extendVector(vec, param):
    """Makes vector param times longer, while holding the first point of vector in place"""
    return [[vec[0][0], vec[0][1]],
            [(vec[1][0] - vec[0][0]) * param + vec[0][0], (vec[1][1] - vec[0][1]) * param + vec[0][1]]]


def sumVectors(vec1, vec2):
    return [[vec1[0][0] + vec2[0][0], vec1[0][1] + vec2[0][1]], [vec1[1][0] + vec2[1][0], vec1[1][1] + vec2[1][1]]]


def shiftVector(vec, dx, dy):
    return [[vec[0][0] + dx, vec[0][1] + dy], [vec[1][0] + dx, vec[1][1] + dy]]


def ifLineBetweenTwoPoints(line, p1, p2):
    angle = lineAngle(line[0], line[1])
    p1 = apply2dRotation(p1, -angle)
    p2 = apply2dRotation(p2, -angle)
    line = rotate2dLine(line[0], line[1], [0, 0], -angle)
    return p1[0] <= line[0][0] <= p2[0] or p2[0] <= line[0][0] <= p1[0]


def flipPointOverLine(point, line, otherSideDistance = 2):
    angle = lineAngle(line[0], line[1])
    apply2dRotation(point, -angle)
    line = rotate2dLine(line[0], line[1], [0, 0], -angle)
    p = [-otherSideDistance * point[0] / abs(point[0]) + line[0][0], point[1]]
    apply2dRotation(p, angle)
    return p

# print(movePointAwayFromSurface([0.5, 0.5], [[0, 0], [1, 1]], 1))

# print(surfaceContainsPointShadow([[950, 330], [800, 500]], [900, 430]))

# lineTangentToPoints([-2.3, 0], [0, 1])
# print(lineAngle([-1, -1], [1, 1]))


# point = [400, 400]
# segment = [[440, 358], [343, 470]]
# print(pointToSegmentDistance(segment, point))

# print(pointToSegmentDistance([[0, 0], [1, 0]], [2, 0.5]))

# l = 100
# for i in range(l):
#     angle = i / l * 2 * math.pi
#     print("angle:", angle, "line angle:", lineAngle(rotate2dLine([0, 0], [0, -1], [0, 0], angle)[0], rotate2dLine([0, 0], [0, -1], [0, 0], angle)[1]))

# print(rotate2dLine([0, 0], [0, -1], [0, 0], math.pi/2))

# print(lineAngle([0, 0], [0, -1]))
# print(lineAngle([0, 0], [1, -1]))
# print(lineAngle([0, 0], [1, 0]))
# print(lineAngle([0, 0], [1, 1]))
# print(lineAngle([0, 0], [0, 1]))
