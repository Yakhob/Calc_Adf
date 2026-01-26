def evaluate_expression(expression):
    """
    Evaluate a mathematical expression using BODMAS rules
    Supports +, -, *, /, %, parentheses ()
    """

    tokens = tokenize(expression)
    values = []     # number stack
    operators = []  # operator stack

    i = 0
    
    while i < len(tokens):  #main loop
        token = tokens[i]

        # If token is a number
        if isinstance(token, (int, float)):
            values.append(token)

        # If token is opening bracket
        elif token == '(':
            operators.append(token)

        # If token is closing bracket
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(values, operators)
            operators.pop()  # remove '('

        # If token is an operator
        else:
            while (operators and
                   operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(token)):
                apply_operator(values, operators)
            operators.append(token)

        i += 1

    # Apply remaining operators
    while operators:
        apply_operator(values, operators)

    return values[0]


# ---------------- Helper Functions ---------------- #

def tokenize(expression):
    """
    Converts expression string into numbers and operators
    """
    tokens = []
    num = ""

    for char in expression.replace(" ", ""):
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(float(num) if '.' in num else int(num))
                num = ""
            tokens.append(char)

    if num:
        tokens.append(float(num) if '.' in num else int(num))

    return tokens


def precedence(op):
    """
    Returns precedence of operators
    """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    return 0


def apply_operator(values, operators):
    """
    Applies an operator to the top two values
    """
    right = values.pop()
    left = values.pop()
    op = operators.pop()

    if op == '+':
        values.append(left + right)
    elif op == '-':
        values.append(left - right)
    elif op == '*':
        values.append(left * right)
    elif op == '/':
        if right == 0:
            raise ValueError("Division by zero")
        values.append(left / right)
    elif op == '%':
        if right == 0:
            raise ValueError("Modulus by zero")
        values.append(left % right)
