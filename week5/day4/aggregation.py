import numpy as np
"""
## 1. Drill

Consider:

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

offset = np.array([10, 20, 30])

Predict: matrix + offset

np.array([
    [1, 2, 3],
    [4, 5, 6],
    [10, 20, 30],
])

Why might it work?
Both the arrays that we are adding are of same dimension on the other axis (say 'Y')

Result: 
np.array([
    [11 22 33], 
    [14 25 36], 
])
Now consider:

offset = np.array([10, 20])

Would the operation work? Why?
No, this would not work as there only 2 elements in this array.
"""

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

offset = np.array([10, 20, 30])
print(matrix + offset)

# offset = np.array([10, 20])
# print(matrix + offset)

"""
## 2. Learn the basic idea of broadcasting:

> NumPy can align compatible shapes so an operation can be applied
> without explicitly creating repeated data.

Explore:

``` python
np.sum(matrix)
np.sum(matrix, axis=0)
np.sum(matrix, axis=1)

np.mean(matrix)
np.min(matrix)
np.max(matrix)
```

Mental model for a 2D array: - `axis=0` → operate down rows, producing
one result per column - `axis=1` → operate across columns, producing one
result per row

Verify this with small arrays instead of only memorising it.

"""

print(np.sum(matrix))           # Returns sum of all items in the matrix
print(np.sum(matrix, axis=0))   # Sum of all items on one axis (columns)
print(type(np.sum(matrix, axis=0)))
print(np.sum(matrix, axis=1))   # Sum of all items on other axis (rows)

print(np.mean(matrix))          # Average of all items in the matrix
print(np.min(matrix))           # Minimum of all items in the matrix
print(np.max(matrix))           # Maximum of all items in the matrix

print(np.std(matrix))           # Standard deviation of all the times in the matrix
print(np.std(matrix, axis=0))   # Standard deviation across one axis similar to the sum above
print(np.std(matrix, axis=1))

print(np.var(matrix))           # statistical variance of the elements in an array
print(np.array([1.]).dtype)
print(np.mean(np.empty((0, 2))))
print(np.array([]).ndim)


def column_statistics(matri):
    """
    Return the mean of each column
    :param matri: 2D numeric NumPy array.
    :return: 1D NumPy array containing column means.
        "empty arrays - np.array of nan"
        "zero-row arrays - nan"
        "one-row arrays - average of the row"
        "one-column arrays - average of the column"
        "negative values - average to be returned if the dimension conditions match"
        "invalid dimensionality - None"
        "non-numeric data - None"
    """
    # 1. Catch invalid types and dimensions immediately
    if not isinstance(matri, np.ndarray) or matri.ndim not in (1, 2) or matri.dtype.kind not in 'iuf':
        return None

    # 2. Catch 1D empty arrays -> None
    if matri.ndim == 1 and matri.size == 0:
        return None

    # 3. Catch 2D zero-row arrays -> Return an array of NaNs matching the column count
    if matri.ndim == 2 and matri.shape[0] == 0:
        return np.full(matri.shape[1], np.nan)

    # 4. Standard calculation for valid 1D or 2D arrays
    return np.mean(matri, axis=0)


"""
Reflection: 

1.  What does `axis=0` mean for a 2D array?
It is the data column wise i.e, if I arrange 1 to 9 in a 3 X 3 matrix writing 1, 2, 3 in first line and 4, 5, 6 in 
second line and the remaining in the last line then axis=0 will have 1, 4, 7

2.  What does `axis=1` mean?
In the same matrix axis=1 for first row is 1, 2, 3. 

3.  Why did broadcasting work with a length-3 array?
The cardinality should match for broadcasting.

4.  Why did length-2 create a shape problem?
Because the cardinality did not match, it wouldn't know what to do with the 3rd column.

5.  When should shape mismatch make you reconsider the data model?
If cases were broadcasting/masking is required and shapes do not match, we have to ensure shapes are matching.
"""
