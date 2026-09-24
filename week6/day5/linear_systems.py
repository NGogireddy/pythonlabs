import numpy as np

"""
## 1. Drill 

v = np.array([3.0, 4.0])

What is the geometric length of this vector? 5.0

np.linalg.norm(v)

Now consider the system:

2x + y = 5
x  - y = 1

Can you solve it manually?  x -> 2 and y -> 1

"""

v = np.array([3.0, 4.0])
print(np.linalg.norm(v))

"""
## 2. Learn 

np.linalg.norm(...) -> Gives the distance of the vector from the origin (0,0,...) depending the on the dimensions

A x = b
Learn: np.linalg.solve(A, b)

"""

v1 = np.array([3.0, 4.0, 7., 12.])
print(np.linalg.norm(v1))

A = np.array([[2, 1], [1, -1]])
b = np.array([5, 1])
x = np.linalg.solve(A, b)

print(x)

B = np.array([[2, -1, 3], [3, 1, -1], [1, 2, 1]])
c = np.array([11, 8, 7])
y = np.linalg.solve(B, c)

print(y)

C = np.array([[2, -1], [1, 1]])
d = np.array([5, 4, 5])
# z = np.linalg.solve(C, d) --> Input matrix should be a square matrix and the dimenstions of final vector should align

# print(z)


def solve_linear_system(matrix, vector):
    """
    Finds the vector that transforms the matrix to the given input vector
    :param matrix: A 2D numerical matrix in np array
    :param vector: A numerical vector in np array (1D)
    :return: 1D np array that transforms matrix to this output, if invalid input it returns none
    """
    if isinstance(matrix, np.ndarray) and matrix.ndim == 2 and matrix.dtype.kind in 'iuf':
        if isinstance(vector, np.ndarray) and vector.ndim == 1 and vector.dtype.kind in 'iuf':
            if matrix.shape[0] == matrix.shape[1] and matrix.shape[0] == vector.shape[0]:
                det = np.linalg.det(matrix)
                if not np.isclose(det, 0):
                    return np.linalg.solve(matrix, vector)
    return None


"""
## 5. Reflect 
1.  What is a vector norm?
It is the distance of that point from the origin. 

2.  What does `A x = b` mean?
Matrix 'A' transforms the vector 'x' into vector 'b'

3.  What does `np.linalg.solve` return?
It finds the vector that gets transformed into the final vector for the given Matrix.

4.  Why should singular matrices be part of your contract?
Singlular matrices are not inversible?? i.e, we cannot solve the equations if they are singular. 

5.  Why is explicit validation important for numerical functions?
Without this validation, the jobs will through runtime errors of invalid data types. 
"""
