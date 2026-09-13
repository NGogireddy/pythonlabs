import numpy as np

"""
Initializing various dimension arrays to np array objects and understanding the methods and features
"""

# One dimension arrays

a = np.array([0, 1, 2, 4])
print("\nDisplaying 1d array and their attributes")
print(a)                # prints the array
print(a.shape)          # Prints the shape of the array
print(a.ndim)           # Prints how many dimensions the array has got
print(a.size)           # Total number of items in the array
print(a.dtype)          # Data type of the array. We cannot mix the data types in np.
print(a.itemsize)       # Size of each item in the array.
print(a.strides)        # Number of bytes it need to move to get to the next item.
print(a.flags)          # Checks if the data is contiguous in the memory

# Two dimension arrays

b = np.array([range(3), range(3,6)], dtype=np.int16)
print("\nDisplaying 2d array and their attributes")
print(b)
print(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)
print(b.itemsize)
print(b.strides)        # Number of bytes it need to move in both directions to get to the next item.
print(b.flags)

# Three dimenstion arrays

c = np.arange(24).reshape(2, 3, 4)    # Can reshape the array
print("\nDisplaying 3d array and their attributes")
print(c)
print(c.shape)
print(c.ndim)
print(c.size)
print(c.dtype)
print(c.itemsize)
print(c.strides)
print(c.flags)

d = c.reshape(4, 6)
print('\nReshaped to a 2d array of 4*6')
print(d)
print(2*d)              # doubles each element in the array
print(2+d)              # Adds two to each element in the array
print(d**2)             # Squares each element
print(type(d))
print(d.flags)

e = np.array([[1, 2, 3], [7, 8, 9]], dtype=np.complex64)
print('\nWorking on complex numbers in Numpy')
print(e)
print(2*e)
print(e**2)
print(e.strides)
print(e.flags)

# Mathematical operations on Numpy arrays

a1 = np.array([range(3), range(3,6), range(6,9)], dtype=np.int32)
a2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.int32)
print('\nWorking on the below two arrays')
print(a1)
print()
print(a2)
print()
print(f'a1 + a2: \n {a1 + a2}')     # Individual elements added in each position
print(f'a1 * a2: \n {a1 * a2}')     # Individual elements multiplied in each position not like matrix
print(f'a1 @ a2: \n {a1 @ a2}')     # Dot product, similar to matrix multiplication
print(f'a1.strides is: {a1.strides}')

copy_a = a.copy()
print('\nCopied data from a, verifying the flags')
print(copy_a)
print(copy_a.flags)                 # Copy gets its owndata
copy_a[0] = 5
print(f'copy_a after modifying: {copy_a}')
print(f'a after modifying copy_a: {a}')

view_a = a.view()
print('\nCreated a view of data from a, verifying the flags')
print(view_a)
print(view_a.flags)                 # View gets a pointer to the original data.
view_a[0] = 9
print(f'view_a after modifying: {view_a}')
print(f'a after modifying view_a: {a}')

slice_a = a[:2]
print('\nSliced one dimension array a for first two elements')
print(slice_a)                      # Slice creates a view of the original data and gives the pointer to that metadata
print(slice_a.flags)
slice_a[0] = 1      # Modifying the first element of slice_a
print(f'slice_a after modifying the data: {slice_a}')
print(f'Original a after modifying its slice: {a}')

print(f"\nSlicing the following 2d:\n {b}")
print(f'\nSliced 2d array for all rows and 1st 2 columns using  b[:,:2]:\n {b[:, :2]}')
print(f'\nSliced 2d array for all rows and last 2 columns using b[:, 1:]:\n {b[:, 1:]}')
print(f'\nSliced 2d array for everything in the 3rd column using b[:,2]:\n {b[:, 2]}')

print(f"\nSlicing the following 3d:\n {c}")
print(f'\nSliced 2d array for all rows on first axis, 2nd row onwards on second axis and 2nd and 3rd on last axis '
      f'using c[:, 1:, 1:3]:\n {c[:, 1:, 1:3]}')
# c[:, 1:, 1:3] -> First argument (:) is to pick everthing on the first axis, second argument (1:) is to pick
# everything from index 1 onwards and the last argument (1:3) is to pick second and 3rd row contents on the last axis
# a:b on every axis a -> starting index (inclusive), b -> ending index (exclusive)


def manipulate_array_memory(arr: np.ndarray, structural_change: bool) -> np.ndarray:
    """
    Modifies or returns a structural representation of an input array based on safety flags.

    CONTRACT:
    - Input:
        - arr: A non-empty, contiguous 1D or 2D np.ndarray.
        - structural_change: bool. If True, returns a shallow memory view with a modified shape.
                             If False, returns a completely isolated deep copy.
    - Output: Returns a np.ndarray.
    - Invalid Input / Exceptions:
        - Raises TypeError if arr is not an instance of np.ndarray.
        - Raises ValueError if arr is empty (size == 0).
    - Side-Effects: None. Modifying the output of a deep copy must not mutate the original `arr`.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a valid NumPy ndarray.")
    if arr.size == 0:
        raise ValueError("Cannot process an empty array.")

    if structural_change:
        # Return a view flattened if 2D, or expanded if 1D
        if arr.shape[0] > 1:
            return arr.ravel()
        else:
            return arr.reshape(-1, 1)
    return arr.copy()


view_a1 = manipulate_array_memory(a1, True)
print(f'Called manipulate_array_memory for True')
print(view_a1)
print(view_a1.flags)

copy_a1 = manipulate_array_memory(a1, False)
print(f'Called manipulate_array_memory for False')
print(copy_a1)
print(copy_a1.flags)

