import numpy as np

"""
## 1. Drill

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

Prediction:

A.T -> np.array([
    [1, 4] 
    [2, 5],
    [3, 6],
])
A.T.shape   -> (3, 2)

Then consider:
I = np.eye(3)      -> Identity Matrix??

A @ I              -> A

All predictions are true. 
"""

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])


print(A.T)
print(A.T.shape)

I = np.eye(3)
print(I)
print(A @ I)

print(np.transpose(A))
print('after np.transpose on A')
print(A)
print('A.T and np.transpose(A), both do not change the original matrix')


"""
## 2. Learn 

A.T
np.transpose(A)
np.eye(n)

(m, n) → transpose → (n, m)


A @ I = A
I @ A = A  


A == A.T        -> e.g I is a symmetric matrix, np.array([[1, 2, 3], [2, 4, 5], [3, 5, 7]])

"""

B = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 7]])
print(B)
print(B.T)


def is_symmetric(matrix):
    """
    Returns True if the matrix is a 2D numpy numeric symmetric, otherwise False
    :param matrix: 2D numpy numeric array
    :return: Boolean
    """
    if isinstance(matrix, np.ndarray) and matrix.ndim == 2 and matrix.dtype.kind in 'iuf':
        if matrix.shape[0] == matrix.shape[1]:
            return np.allclose(matrix, matrix.T)
    return False


"""
## 5. Reflection

1.  What does transpose do to shape?
It inverts the matrices from rows to columns and columns to rows. A (m, n) shape changes to (n, m)

2.  What makes a matrix symmetric?
When a matrix and its Transpose is same then it is symmetric i.e, it doesn't change the way you look at the matrix row
first or column first. 

3.  Why is the identity matrix useful?
Need to understand the real world scenario where it helps.

4.  Why might floating-point equality require tolerance?
The way python stores the floating point numbers is not what exactly we see. It is always close to the actual number. 

5.  Why must `is_symmetric` require a square matrix?
symmetric is when you see the matrix either ways looks same, it they need to be same it should be a square matrix.
"""