def gcd(a, b):
    """
    Finds Greatest Common Divisor using Euclidean Algorithm
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def simplify(numerator, denominator):
    """
    Simplifies a fraction
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")

    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def add_fractions(f1, f2):
    """
    Adds two fractions
    f1, f2 -> (numerator, denominator)
    """
    n1, d1 = f1
    n2, d2 = f2

    numerator = n1 * d2 + n2 * d1
    denominator = d1 * d2
    return simplify(numerator, denominator)


def subtract_fractions(f1, f2):
    """
    Subtracts two fractions
    """
    n1, d1 = f1
    n2, d2 = f2

    numerator = n1 * d2 - n2 * d1
    denominator = d1 * d2
    return simplify(numerator, denominator)


def multiply_fractions(f1, f2):
    """
    Multiplies two fractions
    """
    n1, d1 = f1
    n2, d2 = f2

    numerator = n1 * n2
    denominator = d1 * d2
    return simplify(numerator, denominator)


def divide_fractions(f1, f2):
    """
    Divides two fractions
    """
    n1, d1 = f1
    n2, d2 = f2

    if n2 == 0:
        raise ValueError("Cannot divide by zero fraction")

    numerator = n1 * d2
    denominator = d1 * n2
    return simplify(numerator, denominator)


def fraction_to_decimal(fraction):
    """
    Converts fraction to decimal
    """
    numerator, denominator = fraction
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return numerator / denominator
