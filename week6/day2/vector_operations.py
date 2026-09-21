import numpy as np

"""
## 1. Drill 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

Prediction:

a + b   -> np.array([5, 7, 9])      # vector addition
a * b   -> np.array([4, 10, 18])    # vector multiplication
2 * a   -> np.array([2, 4, 6])      # scalar multiplication

Now think about:

np.dot(a, b)    -> 32           # similar to the matrix multiplication

What type of result should a dot product produce?
Dot product produces the result of a matrix multiplication. 

"""

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a+b)
print(a*b)
print(a*2)
print(np.dot(a,b))
print(a @ b)        # Another notation of dot product

c = np.array([[1, 2], [3, 4]])
d = np.array([[1, 1], [1, 1]])
print(c @ d)        # dot product is the matrix multiplication.
print (c * d)       # element wise multiplication.

# print(c @ a)  -> Raises ValueError as the shape of c is (2, 2) and shape of a is (3, ) we cannot have dot product
# for these shapes.

e = np.array([4, 5])
print(e * c)    # broadcasting is done here as the shapes are (2, 2) and (2, )


def vector_dot_product(a, b):
    """
    Returns the dot product of both the 1D numpy numeric arrays
    :param a: 1D numpy numeric array of shape (n, )
    :param b: 1D numpy numeric array of shape (n, )
    :return: Dot product of both the matrices
    """
    if isinstance(a, np.ndarray) and a.ndim == 1 and a.dtype.kind in 'iuf':
        if isinstance(b, np.ndarray) and b.ndim == 1 and b.dtype.kind in 'iuf':
            if a.size == b.size:
                return a @ b
            else:
                raise ValueError("Both arrays are not of same size")
        raise ValueError("B array is not suitable for dot product")
    raise ValueError("A array is not suitable for dot product")


"""
## 5. Reflection

1.  What is the difference between `*` and `@`?
'*' give the multiplication at element wise and '@' gives the dot product of the matrix.

2.  What does a dot product produce?
If the arrays are 1D then it produces a scalar. 

3.  Why must the vector lengths match?
The vector lengths should match as element wise multiplication is done of '*' and all results were added for '@' after 
the multiplication. 

4.  Why is shape validation useful here?
If shape validation is not done it would raise Error and the program would break abruptly. 

5.  What would happen if you silently accepted mismatched vectors?
The program would stop in the middle with ValueError. 
"""