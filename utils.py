from typing import Any
import numpy as np


def validate_fixed_matrix(mat: Any) -> bool:
    """
    Ensure that the user entered a correct matrix input.
    :param mat: Any. Matrix for the calculation.
    :return: True if the matrix is in the right format, False otherwise.
    """
    # convert to list of elements, separated by ','
    mat_array = mat.split(',')

    # must include only numeric elements
    for element in mat_array:
        try:
            int(element)
        except Exception as e:
            print(e)
            return False

    # must be squared matrix
    sqrt = np.sqrt(len(mat_array))
    if sqrt != int(sqrt):
        return False

    # after all "tests" passed successfully - return True
    return True


def convert_raw_matrix_to_real_matrix(mat: str) -> np.array:
    """
    convert the raw string of the matrix to Numpy object that available for calculations.
    :param mat: str.
    :return: np.array.
    """
    # divide by ','
    numbers_list = mat.split(',')
    # get the sqrt value for the matrix building
    sqrt_value = int(np.sqrt(len(numbers_list)))
    # build the matrix
    matrix = np.array(numbers_list, dtype=np.int64).reshape(sqrt_value, sqrt_value)
    return matrix


def matrices_calc(operation: str, mat1: np.array, mat2: np.array) -> np.array:
    """
    Returns the result of the chosen calculation and two matrices.
    """
    if operation.lower() == 'add':
        return np.add(mat1, mat2)
    elif operation.lower() == 'multiply':
        return np.dot(mat1, mat2)
    else:
        raise ValueError('Unavailable operation')


