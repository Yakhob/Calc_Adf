import math


def natural_log(value):
    """
    Calculates natural logarithm (ln)
    """
    if value <= 0:
        raise ValueError("Natural logarithm is defined only for positive numbers")
    return math.log(value)


def common_log(value):
    """
    Calculates common logarithm (log base 10)
    """
    if value <= 0:
        raise ValueError("Logarithm is defined only for positive numbers")
    return math.log10(value)


def log_base(value, base):
    """
    Calculates logarithm with custom base
    """
    if value <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid value or base for logarithm")
    return math.log(value, base)
