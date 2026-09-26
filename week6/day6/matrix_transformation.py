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
            if len(vectors.shape) == 1:
                yield matrix @ vectors
            for vector in vectors:
                yield matrix @ vector


def collect_transformed_vectors(matrix=np.empty([0]), vectors=np.empty([0])):
    stream = transform_vectors(matrix, vectors)
    return [vector for vector in stream]


def transform_vectors_alternative(matrix, vectors):
    if is_valid(matrix) and is_valid(vectors):
        if is_compatible(matrix.shape, vectors.shape):
            return (matrix @ vectors.T).T


if __name__ == "__main__":
    output = collect_transformed_vectors()

"""
Reflection: 

1.  What is the matrix shape?
The matrix should be a 2 dimensional square matrix which is not singular. 

2.  What is the vector shape?
The shape of the vector should have the dimensions equal to the size of the matrix i.e 3X3 matrix should have vector of
length 3. 

3.  Why is the multiplication valid?
multiplication always happens on the inner dimension (m, n) @ (n, p) --> (m, p)

4.  What is the output shape?
(m, n) @ (n, p) --> (m, p)

5.  Where is validation performed?
validations are performed before the actual multiplication is done. 

6.  Where is the numerical calculation performed?
All of these should be performed after the validations and compatibility check. 

7.  Are any unnecessary copies created?
No unnecessary copies are created. 

8.  What happens with 10 vectors?
Two approaches are coded here, one with yield and the other with numpy Transpose feature. With 10 vectors the run time
is not much effected. 

9.  What happens with 100,000 vectors?
The yield option runs very slow compared to the numpy Transpose feature. However the memory utilized will peak for the 
run time during the calculation. 

10. What is the dominant computational cost?
In the looping method the cost would be for the execution time as well as the memory for the consolidated list. For the
Transpose and dot product option, it would be the peak memory cost. 
 
11. What would you change before production?
I would add few more test cases using the empty arrays, floating numbers, negative numbers etc., 
"""