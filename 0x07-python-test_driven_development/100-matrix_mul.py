#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(matrix_a, matrix_b):
    """Multiply two matrices.

    Args:
        matrix_a (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.
        
    Raises:
        TypeError: If either matrix_a or matrix_b is not a list of lists of ints/floats.
        TypeError: If either matrix_a or matrix_b is empty.
        TypeError: If either matrix_a or matrix_b has different-sized rows.
        ValueError: If matrix_a and matrix_b cannot be multiplied.
        
    Returns:
        A new matrix representing the multiplication of matrix_a by matrix_b.
    """

    if matrix_a == [] or matrix_a == [[]]:
        raise ValueError("matrix_a can't be empty")
    if matrix_b == [] or matrix_b == [[]]:
        raise ValueError("matrix_b can't be empty")

    if not isinstance(matrix_a, list):
        raise TypeError("matrix_a must be a list")
    if not isinstance(matrix_b, list):
        raise TypeError("matrix_b must be a list")

    if not all(isinstance(row, list) for row in matrix_a):
        raise TypeError("matrix_a must be a list of lists")
    if not all(isinstance(row, list) for row in matrix_b):
        raise TypeError("matrix_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in matrix_a for num in row]):
        raise TypeError("matrix_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in matrix_b for num in row]):
        raise TypeError("matrix_b should contain only integers or floats")

    if not all(len(row) == len(matrix_a[0]) for row in matrix_a):
        raise TypeError("each row of matrix_a must should be of the same size")
    if not all(len(row) == len(matrix_b[0]) for row in matrix_b):
        raise TypeError("each row of matrix_b must should be of the same size")

    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("matrix_a and matrix_b can't be multiplied")

    inverted_b = []
    for r in range(len(matrix_b[0])):
        new_row = []
        for c in range(len(matrix_b)):
            new_row.append(matrix_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in matrix_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
