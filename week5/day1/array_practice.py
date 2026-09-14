"""
predict:

For `[1, 2, 3, 4]`: - number of elements? - dimensions? - shape?
Number of Elements: 4
Dimension: 1d
Shape: 1X4

For:
1 2 3
4 5 6

shape: 2d
dimensions: 2X4
number of elements: 6

What happens with:

``` python
values = [1, 2, 3]
values * 2
```
Prediction: It should error out.
Actual: It doubles the list by adding the same elements at the end.

What would you expect from:

``` python
import numpy as np
values = np.array([1, 2, 3])
values * 2
```
Prediction: Multiply every value by 2.
Result: It is correct, but note that it will not change the values in the variable
"""

import numpy as np
from collections import defaultdict
values = np.array([1, 2, 3, 4])

print(values.shape)     # Gives the shape of values i.e number of items in values
print(values.ndim)      # Number of dimensions in the array. It is 1 here
print(values.size)      # Total number of items in the array
print(values.dtype)     # Data type of the array. We cannot give multiple data types in numpy array.

print(np.zeros(5))      # Gives a numpy array of 5 elements initialized with zeroes.
print(np.ones(5))       # Gives a numpy array of 5 elements initialized with ones.
print(np.arange(5))     # Gives a numpy array of 5 elements starting with 0 (similar to range).
print(np.arange(2, 10, 3))  # Gives a numpy array of all elements between 2 and 10 in the steps of 3 (similar to range).

"""
Create a 2D array and inspect its properties.
"""

twod_array = np.arange(6).reshape(2, 3)
print(twod_array)
print(twod_array.shape)
print(twod_array.ndim)
print(twod_array.size)
print(twod_array.dtype)
print(twod_array.strides)   # The number of bytes it need to move in a direction to get to the next item. here it is
# 24 to the down and 8 to the right


def describe_array(value):
    """
    Receives a Numpy ndarray and returns the properties of the array in a dictionary. If it is not numpy array raise
    TypeError exception
    :param value:
    :return:
    """
    if isinstance(value, np.ndarray):
        output = defaultdict(str)
        output["shape"] = value.shape
        output["ndim"] = value.ndim
        output["size"] = value.size
        output["dtype"] = value.dtype
        return output
    else:
        raise TypeError


"""
Reflection: 
Why is shape important?         Shape tells us about how the items are organised in the array.
What does ndim tell you?        ndim gives us how many dimensions are there in the array. 
What does size tell you?        size tells us how many total items are present in the array
Why does dtype matter?          dtype tells about the data type of the items present in the array. 
When might a Python list still be more appropriate?     List is appropriate where you want to expand on the items or 
have mixed type of items in the list. 
"""
