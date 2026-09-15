import numpy as np
"""
## 1. Drill

For `[1, 2, 3, 4]`, describe the Python-loop approach for doubling every value.

It takes the first element, applies the double logic on it and returns it, then moves on to the next one and returns,
the process is repeated until all elements are exhausted.

Then ask how the same operation could be expressed with a NumPy array.

In numpy the doubling is performed on all the elements at once.

Predict:

values = np.array([0.2, 0.7, 0.4, 0.9])
values > 0.5

Ans: [False, True, False, True]

And:

values[values > 0.5]
Ans: No clue
"""

values = np.array([0.2, 0.7, 0.4, 0.9])
print(values > 0.5)
print(values[values > 0.5])         # filters all the elements where the condition is true -> boolean masking

"""
## 2. Learn 

Learn: - element-wise arithmetic - array/scalar operations - comparisons - boolean arrays - boolean masks 
- why vectorisation is useful 
- why vectorisation is not automatically the answer to every problem

Explore:

values * 2              # Doubles every value in the array
values + 10             # Adds 10 to all values in the array
values / 2              # Halves the values in the array
values > 0.5            # Verifies each value is > 0.5 and returns True or False list for all the values in the array
values[values > 0.5]    # Filters out the values less than 0.5 from the array
"""


def normalise_values(values, minimum, maximum):
    """
    Normalize the values in the vector Map (`[minimum, maximum]` to `[0, 1]`)
    :param values: 1D numpy array
    :param minimum: minimum value to normalize
    :param maximum: maximum value to normalize
    :return: normalized np array between [0, 1] i.e, Map `[minimum, maximum]` to `[0, 1]` works for int and float values
    Empty values returns None.
    minimum >= maximum returns None
    Any other input other than 1D numpy arrays return none
    """
    if minimum < maximum and isinstance(values, np.ndarray) and values.ndim == 1:
        ran = maximum - minimum
        output = (values-minimum)/ran
        return output


"""
Reflection: 

1.  What does vectorisation mean in your own words?
It is a powerful tool to apply an operation on all the elements in the array. 

2.  Why can it be faster than a Python loop?
It does not use the for loop to iterate through all the elements, it directly apply the operation at once. 

3.  Does vectorised automatically mean better?
No, it depends on what operation is being performed. For e.g, If we are performing a task that depends on what is there 
before and after the current element, vectorisation is not a good choice. 

4.  What is a boolean mask?
It is a mask applied on all the elements in the ndarray. Technique used to filter rouge values. 

5.  What does `values[mask]` mean conceptually?
Apply the mask on each item on values and if the mask is false, filter out the element. 

I haven't used assert_allcose today in the practice as it is failing for Nonetype outputs. assert_array_equal is working
here hence left it. However I understand to compare the floating point results we have to use assert_allclose. 
Ideal way to handle this is to separate the test case into two where Nonetype scenarios are checked separately
"""
