"""
## 1. Drill
import numpy as np

a = np.array([1, 2, 3])
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

Prediction:
a.shape         -> (3,)
a.ndim          -> 1
b.shape         -> (2, 3)
b.ndim          -> 2


Then predict the shape of:

column = np.array([
    [1],
    [2],
    [3],
])

Prediction:       -> Shape -> (3, 1),  ndim -> 2

> Is `[1, 2, 3]` the same shape as `[[1], [2], [3]]`?

They contain similar values, but they are not the same NumPy object
structure.

"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(a.shape)
print(a.ndim)
print(b.shape)
print(b.ndim)

column = np.array([
    [1],
    [2],
    [3],
])

print(column.shape)
print(column.ndim)

"""
## 2. Learn:

-   scalar
-   1D vector
-   2D row vector
-   2D column vector
-   matrix
-   shape as part of the mathematical meaning

Explore:

v = np.array([1, 2, 3])
row = np.array([[1, 2, 3]])
column = np.array([
    [1],
    [2],
    [3],
])

Compare:

v.shape         (3, )
row.shape       (1, 3)
column.shape    (3, 1)

Also investigate:

v.reshape(3, 1)
v.reshape(1, 3)
"""

v = np.array([1, 2, 3])
row = np.array([[1, 2, 3]])
column = np.array([
    [1],
    [2],
    [3],
])

print(v.shape, row.shape, column.shape)
print(v.reshape(3, 1))
print(v.reshape(1,3))
print(v)

print(b.reshape(3, 2))  # Reshape will put all the elements in a row and then reshape them as requested.
                        # It is not a transpose of the original matrix


def describe_vector(values):
    """
    Accepts a np array and determines the length, shape and ndim of the array. Any invalid input returns dictionary
    with zero values.
    :param values: A NumPy ndarray, exactly one-dimensional, numeric dtype, non-empty
    :return: {"length": ..., "shape": ..., "dtype": ... }
    """
    output = {"length": 0, "shape": 0, "dtype": "" }
    if isinstance(values, np.ndarray) and values.ndim == 1 and values.dtype.kind in 'iuf' and values.size > 0:
        output["length"] = values.size
        output["shape"] = values.shape
        output["dtype"] = values.dtype
    return output


"""
## 5. Reflection

1.  What is the difference between a vector and a matrix?
A vector is a set of values representing a point in space. A matrix of one row or column can be used to represent a 
vector. A matrix of 2 dimensions will represent multiple vectors. 

2.  Why is `(3,)` different from `(3, 1)`?
(3, ) is one dimension np array and (3, 1) is a two dimension np array. 

3.  Why does shape matter in linear algebra?
The shape in linear algebra represents the direction of the vector and change in the shape can mis-represent the vector

4.  What is a column vector?
A column vector is also a vector represented in columns. 

5.  Why might NumPy's 1D arrays require extra care when doing linear algebra?
In linear algebra the shape matters the most for arithmatic operations. The dot products and other operations will not
be successful when the shapes are not aligned. 

"""