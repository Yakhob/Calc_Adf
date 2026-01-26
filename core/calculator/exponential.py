import math


def exponential(value):
    """
    Calculates e^x
    """
    return math.exp(value)


def power(base, exponent):
    """
    Calculates base raised to the power exponent
    """
    return base ** exponent


def inverse_exponential(value):
    """
    Inverse of exponential function (natural logarithm)
    """
    if value <= 0:
        raise ValueError("Inverse exponential is defined only for positive numbers")
    return math.log(value)
