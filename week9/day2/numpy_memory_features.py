import numpy as np

"""
## Drill

Create a NumPy array, take a slice, modify the slice, and observe the original array.

Then repeat with `.copy()`.

Predict the outcome before running each version.
"""

a1 = np.array([1, 2, 3, 4, 5])
a2 = a1[0:2]
a3 = a1[2:]
print("Original array and slices")
print(a1, a2, a3)

a2[1] = 1
a3[2] = 4

print("Array after changes")
print(a1, a2, a3)


b1 = a1[0:4].copy()
print("Copied array")
print(b1)

b1[0] = 6
print(f"Modified array copy: {b1}")
print(f"Original array:{a1}")

c1 = a1.view()
print("Working with views now")
print(c1)
c1[0] = 9
print(f"Modified array view: {c1}")
print(f"Original array:{a1}")

"""
slicing and view will use the same internal storage for the elements and any changes to the original or the new sliced/
view object will reflect in the other element. 
copy will create an entirely new copy of the array and will not change anything in the original variable. 
"""

"""
Review:

-   slicing         - returns a slice of the original array. Modifications will be reflected in original array
-   views vs. copies - views behave same as slicing except that it refers the whole array. Copies create a copy, they 
   do not impact the original array items when changed in the copy.  
-   `.copy()`
-   `np.shares_memory()` - Helps to check if the internal memory is shared. 
-   `shape`, - returns the shape of the array as a tuple
-   `strides`, - returns the number of bytes to be skipped to get to the next row, column
-   `nbytes` - the total bytes used for storing the array. 

"""


def return_first_n_rows(arr, n):
    """
    Returns the first n rows of the array as a copy, do not share the memory with the original array.
    arr is a 2d numpy array, if not returns empty array
    if n <= 0 return empty array
    if n >= arr.shape[0] i.e, number of rows less than n, return all rows.
    n should be castable to an integer otherwise returns empty array.
    :param arr: 2d numpy array
    :return: np array
    """
    try:
        rows = int(n)
    except (ValueError, TypeError):
        return np.empty((0, 2))
    if rows <= 0 or not (isinstance(arr, np.ndarray) and arr.ndim == 2):
        return np.empty((0, 2))
    return arr[0:n].copy()


"""
> When might returning a view be useful, and when might returning a copy be safer?
This depends on the use case. In most of the scenarios it is ideal to return a copy of the output. If the intended 
outcome of the function is to filter the input array and return a subset that they need to work on then returning a 
slice or view is helpful. 
"""
