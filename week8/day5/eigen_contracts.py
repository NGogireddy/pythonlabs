import numpy as np

"""
## Drill
For a matrix:

A = [[2, 0],
     [0, 3]]

Prediction:
-   how many eigenvalues you expect         -> 2 Eigen values
-   what the eigenvectors might look like   -> Following are the eigen vectors [1 0] and [0 1]
-   what happens when the matrix acts on each eigenvector   -> The direction of the transformed vector 
remains same and only the magnitude changes. 
"""

"""
## Learn

Think about contracts for a function that calculates eigen-information.

Questions:
-   Must the input be a square matrix?
    Yes the inner two dimensions of the matrix must be a square matrix. 
    
-   What should happen for a non-square matrix?
    For a non square matrix the np.linalg.eig will raise error, we will return None when the inner most 
    matrices are not square matrices
    
-   What dtype should the output use?
    The dtype of the output will be complex numbers, as there are matrices where eigen values are not just
    real numbers. 
    
-   Can eigenvalues/eigenvectors be complex even when the input matrix contains real numbers?
    Yes, they can be complex as well. 
    
-   How should numerical equality be tested?
    As the values returned are floating complex, we should use close/approximation assertions, not equality
    
-   What does the ordering of returned eigenvalues mean?

"""


def is_valid_matrix(mat):
    """
    Validates if the matrix is a np array for which eigen values can be found
    :param mat: np array
    :return: boolean
    """
    if isinstance(mat, np.ndarray) and mat.ndim > 1 and mat.size > 0 and mat.dtype.kind in 'iuf':
        shape = mat.shape
        if shape[-1] == shape[-2]:
            return True
    return False


def calculate_eigen_values(mat=np.empty((2,2))):
    """
    Calculates eigen values for the matrix if it is valid otherwise raises ValueError
    :param mat:
    :return:
    """
    if is_valid_matrix(mat):
        return np.linalg.eig(mat)
    else:
        raise ValueError


if __name__ == '__main__()':
    calculate_eigen_values()

"""
Reflection: 
I have done a lot of study on the transformations to understand the eigen values and eigen vectors. 
Got a good Idea on what eigen vectors are, and the validation rules for the matrix to have eigen values/vectors
How eigen values and vectors are calculated when the dimensions are more than 2 in the input matrix.  

"""