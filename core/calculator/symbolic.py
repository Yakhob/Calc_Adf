from sympy import symbols, Eq, solve, sympify # type: ignore


def solve_expression(expression, variable="x"):
    """
    Solves a symbolic expression.
    Example: "2*x + 3 - 7"
    """
    try:
        var = symbols(variable)
        expr = sympify(expression)
        return solve(expr, var)
    except Exception:
        raise ValueError("Invalid symbolic expression")


def solve_equation(lhs, rhs, variable="x"):
    """
    Solves a symbolic equation.
    Example: lhs="2*x + 3", rhs="7"
    """
    try:
        var = symbols(variable)
        left_expr = sympify(lhs)
        right_expr = sympify(rhs)
        equation = Eq(left_expr, right_expr)
        return solve(equation, var)
    except Exception:
        raise ValueError("Invalid symbolic equation")


def simplify_expression(expression):
    """
    Simplifies a symbolic expression.
    Example: "2*x + 3*x"
    """
    try:
        expr = sympify(expression)
        return expr.simplify()
    except Exception:
        raise ValueError("Invalid expression for simplification")
