import numpy as np


"""
## 1. Drill

For: values = np.array([10, 20, 30, 40, 50])

Prediction:

values[0]       : 10
values[-1]      : 50
values[1:4]     : [20, 30, 40]
values[:3]      : [10, 20, 30]
values[2:]      : [30, 40, 50]

Result: Predictions are correct. This is slicing just like in normal lists

For:

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

Prediction:

matrix[0]       :  [1, 2, 3] 
matrix[:, 1]    :  [2, 5]
matrix[1:, :2]  :  [[4, 5]]

Result: Predictions are correct. [0] is referring to all the items on the first axis. 
[:, 1] is to get everything from each row, but the 1 is asking to get only the 2nd item on each row.
[1:, :2] is to get everything from 2nd row onwards and everything upto 3rd item on it  
"""

values = np.array([10, 20, 30, 40, 50])
print(values[0])
print(values[-1])
print(values[1:4])
print(values[:3])
print(values[2:])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print(matrix[0])
print(matrix[:, 1])
print(matrix[1:, :2])

"""
Learning by experimenting
Learn: - integer indexing - negative indexing - slicing - row/column
selection - `:` notation - views - copies
"""

mat3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print(mat3[1:, :2])      # [[4, 5], [7, 8]
print(mat3[-1, -1])      # 9
print(mat3[::-1, ::-1])  # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

first_row = mat3[0]
print(first_row)
print(first_row.flags)

reverse_matrix = mat3[::-1, ::-1]
print(reverse_matrix)
print(reverse_matrix.flags)
reverse_matrix[0, 0] = 10
print(reverse_matrix)
print(mat3)
# slicing creates metadata for the slice and returns it. If slice is modified the original data in the matrix is updated

mat3_copy = mat3.copy()
print(mat3_copy.flags)
mat3_copy[-1, -1] = 9
print(mat3_copy)
print(mat3)
# copy creates copy of the original matrix and returns it. Changes to the copy will not reflect in the original matrix.


def first_n_rows(matrix, n):
    """
    matrix is a numpy array of 2 dimensions and n is an integer >= 0. In any other case it will raise TypeError
    :param matrix:
    :param n:
    :return: copy of the first n rows in the matrix.
    """
    if isinstance(matrix, np.ndarray):
        if matrix.ndim == 2:
            if isinstance(n, int) and n >= 0:
                return matrix[:n, ].copy()
    raise TypeError


"""
Reflection:
1.  Why are views useful?
    When the matrix is complex and you want to work only on a subset of the matrix then views make it simpler. 
2.  Why can views be dangerous?
    They share the memory of the original matrix and any changes to the views will be modifying the original matrix.
3.  When would you deliberately request a copy?
    If we do not want to accidentally update the original matrix, we should go for copy. 
4.  Why can unnecessary copies matter for large arrays?
    Copies will not share the memory and so will prevent the memory leaks. 
    
I have practiced slicing and it was easy to visualize for 2d arrays but for 3d, it is a bit complex, hopefully when 
working on a production type project it makes sense and easier to process. 
"""
