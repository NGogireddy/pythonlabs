import numpy as np

"""
This mini capstone is about transforming a group of vectors using the matrix provided. 

Input is a matrix of shape (n, n) and one or more vectors of size 'n' in a numpy array. 
Output is the transformed vectors using the matrix. 

Eg: 

Matrix: np.array([
    [4, 5],
    [6, 7]
]) 

Vectors: np.array([
    [1, 3], 
    [1, 0], 
    [0, 1]
])

Result: Transformed vectors in a list: [
    [4*1 + 5*3, 6*1 + 7*3],
    [4*1 + 5*0, 6*1 + 7*0],
    [4*0 + 5*1, 6*0 + 7*1],    
]
"""


def is_valid(arr):
    """
    Checks if the received array is a numerical numpy array
    :param arr: numpy array
    :return: Boolean
    """
    return isinstance(arr, np.ndarray) and arr.dtype.kind in 'iuf'


def is_compatible(mat_shape, vec_shape):
    """
    Checks if the vectors can be transformed with the given matrix.
    :param mat_shape: A tuple having the shape of a matrix
    :param vec_shape: A tuple having the shape of the vector
    :return: Boolean
    """
    if len(mat_shape) == 2 and mat_shape[0] == mat_shape[1]:
        if len(vec_shape) == 1:
            return mat_shape[0] == vec_shape[0]
        elif len(vec_shape) == 2:
            return mat_shape[0] == vec_shape[1]
        else:
            return False
    return False


def transform_vectors(matrix, vectors):
    """
    Function that transforms the vectors using the matrix and yields the transformed vectors
    :param matrix: np.ndarray
    :param vectors: np.ndarray
    :return: np.ndarray
    """
    if is_valid(matrix) and is_valid(vectors):
        if is_compatible(matrix.shape, vectors.shape):
            for vector in vectors:
                yield matrix @ vector


def collect_transformed_vectors(matrix=np.empty([0]), vectors=np.empty([0])):
    stream = transform_vectors(matrix, vectors)
    transformed_vectors = []
    for vector in stream:
        transformed_vectors.append(vector)


if __name__ == "__main__":
    collect_transformed_vectors()
