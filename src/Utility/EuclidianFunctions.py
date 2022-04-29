import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def rotate2dLine(p1, p2, rotationP, angle):
    """Rotates line from p1 to p2 around rotationP by the given angle"""
    start = (p1[0] - rotationP[0], p1[1] - rotationP[1])
    end = (p2[0] - rotationP[0], p2[1] - rotationP[1])

    start = apply2dRotation(start, angle)
    end = apply2dRotation(end, angle)

    start = (start[0] + rotationP[0], start[1] + rotationP[1])
    end = (end[0] + rotationP[0], end[1] + rotationP[1])
    return start, end


def apply2dRotation(vec, angle):
    return (vec[0] * math.cos(angle) - vec[1] * math.sin(angle),
            vec[0] * math.sin(angle) + vec[1] * math.cos(angle))

