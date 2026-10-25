"""Pure facial-landmark measurements used by the webcam application."""
from math import hypot


def _point(point):
    if not hasattr(point, "__len__") or len(point) != 2:
        raise ValueError("Each landmark must contain exactly two coordinates.")
    try:
        return float(point[0]), float(point[1])
    except (TypeError, ValueError) as error:
        raise ValueError("Landmark coordinates must be numeric.") from error


def _distance(first, second):
    x1, y1 = _point(first)
    x2, y2 = _point(second)
    return hypot(x2 - x1, y2 - y1)


def _ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot calculate a ratio with zero horizontal distance.")
    return numerator / denominator


def calculate_ear(eye):
    """Return the eye aspect ratio for six ordered eye landmarks."""
    if len(eye) != 6:
        raise ValueError("EAR requires six eye landmarks.")
    return _ratio(_distance(eye[1], eye[5]) + _distance(eye[2], eye[4]), 2 * _distance(eye[0], eye[3]))


def calculate_mar(mouth):
    """Return the mouth aspect ratio for six ordered mouth landmarks."""
    if len(mouth) != 6:
        raise ValueError("MAR requires six mouth landmarks.")
    return _ratio(_distance(mouth[0], mouth[1]) + _distance(mouth[2], mouth[3]), 2 * _distance(mouth[4], mouth[5]))
