def validate_matrix(matrix):
    """
    Checks if matrix is valid (rectangular)
    """
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Invalid matrix format")


def matrix_addition(A, B):
    """
    Adds two matrices
    """
    validate_matrix(A)
    validate_matrix(B)

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


def matrix_subtraction(A, B):
    """
    Subtracts matrix B from matrix A
    """
    validate_matrix(A)
    validate_matrix(B)

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)

    return result


def matrix_multiplication(A, B):
    """
    Multiplies two matrices
    """
    validate_matrix(A)
    validate_matrix(B)

    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match rows in B")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_value = 0
            for k in range(len(B)):
                sum_value += A[i][k] * B[k][j]
            row.append(sum_value)
        result.append(row)

    return result


def transpose(matrix):
    """
    Returns transpose of a matrix
    """
    validate_matrix(matrix)

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)

    return result
