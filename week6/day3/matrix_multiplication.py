import numpy as np

"""
## 1. Drill 

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])

Prediction:

A.shape     -> (2, 3)
B.shape     -> (3, 2)

(2, 3) @ (3, 2)     -> (2, 2)
(3, 2) @ (2, 1)     -> (3, 1)

A @ B --> [[1*1 + 2*3 + 3*5, 1*2 + 2*4 + 3*6], [4*1 + 5*3 + 6*5, 4*2 + 5*4 + 6*6]]

"""

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])

print(A.shape)
print(B.shape)
print(A@B)
print((A@B).shape)


def multiply_matrices(left=np.empty([0]), right=np.empty([0])):
    """
    If the matrices are not valid for multiplication NoneType is returned.
    :param left: numpy numeric array
    :param right: numpy numeric array
    :return: dot product of left and right array
    """
    if isinstance(left, np.ndarray) and left.ndim == 2 and left.dtype.kind in 'iuf':
        if isinstance(right, np.ndarray) and right.ndim == 2 and right.dtype.kind in 'iuf':
            if left.shape[1] == right.shape[0]:
                return left @ right


"""
## 5. Reflect --- 5 minutes

1.  What is the matrix multiplication shape rule?
A matrix of shape (m, n) can be multiplied with a shape of (n, p) and the result is (m, p)

2.  Why are the inner dimensions important?
Dot product will be applied only if the number of elements are matching. 

3.  What does the output shape represent?
Not sure how to respond to this but the output is (m, p) in the above example. 

4.  Why should you not silently reshape invalid input?
We should not force any multiplication on invalid inputs. 

5.  Why is `@` important for future quantum-computing work?
Dot product is calculation to find the overlaps and probability between different quantum states. 
"""