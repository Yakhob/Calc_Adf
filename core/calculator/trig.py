import math


# ---------------- Angle Conversion ---------------- #

def to_radians(angle, unit):
    """
    Converts angle to radians
    """
    if unit == "degree":
        return angle * (math.pi / 180)
    elif unit == "radian":
        return angle
    else:
        raise ValueError("Unit must be 'degree' or 'radian'")


# ---------------- Trigonometric Functions ---------------- #

def sine(angle, unit="degree"):
    rad = to_radians(angle, unit)
    return math.sin(rad)


def cosine(angle, unit="degree"):
    rad = to_radians(angle, unit)
    return math.cos(rad)


def tangent(angle, unit="degree"):
    rad = to_radians(angle, unit)
    return math.tan(rad)


# ---------------- Inverse Trigonometric Functions ---------------- #

def inverse_sine(value, unit="degree"):
    if value < -1 or value > 1:
        raise ValueError("Input must be between -1 and 1")
    angle = math.asin(value)
    return angle * (180 / math.pi) if unit == "degree" else angle


def inverse_cosine(value, unit="degree"):
    if value < -1 or value > 1:
        raise ValueError("Input must be between -1 and 1")
    angle = math.acos(value)
    return angle * (180 / math.pi) if unit == "degree" else angle


def inverse_tangent(value, unit="degree"):
    angle = math.atan(value)
    return angle * (180 / math.pi) if unit == "degree" else angle
