import numpy as np
from collections import defaultdict

"""
Before coding, define the contract for:

calculate_state_statistics(values)

Write down: - Input - Output - Valid input - Invalid input -
Exceptions - Shape - dtype - Empty input behaviour - Side effects

Input: 
Valid Input: 1D numpy non empty array of dtype numbers (int or float)
Invalid Input: 1D empty np array
               1D np array made of strings
               Any other dimension np array
               Any other data types other than numpy arrays (list, tuples, strings, int, float, string, etc)

Output: 
A dictionary of statistics
{
    "count": int,
    "mean": float,
    "minimum": int/float depending on input dtype,
    "maximum": int/float depending on input dtype,
}

Exceptions: 
    ValueError for empty 1D Inputs or array made of strings
    TypeError for any other invalid inputs

Side Effects: 
    None. Only return the dictionary or raise the exception. 
    Do not write anything log files. 
    Do not modify any inputs
    Do not modify any global state variables.
    
"""

"""
Review: 
    - shape assumptions: Only 1D non empty arrays are valid inputs. 
    - dtype assumptions: Only numeric dtypes are valid
    - floating-point: It is accepted as we can find the mean, min and max
comparison: 
    - empty-array behaviour: This is not a valid input as we do not have any input, statistics cannot be derived.
    - separating validation from calculation: Can be easily done as we have a solid input contract
    - why implicit numerical assumptions can become production defects: If we haven't defined then empty arrays are 
    generally of dtype float64 and these can create issues in the future.  
"""

empty_mat = np.empty((0,2))
print(empty_mat)
print(empty_mat.ndim)
print(empty_mat.shape)
print(empty_mat.size)

zero_mat = np.ones(4)
print(zero_mat)
print(zero_mat.ndim)
print(isinstance(zero_mat, np.ndarray))
print(zero_mat.dtype)
print(zero_mat.size)

arr = np.arange(5)
print(arr.mean())


def calculate_state_statistics(values):
    """
    :param values: 1D numeric dtype non empty numpy arrays
    :return: dictionary of statistics
    """
    if isinstance(values, np.ndarray) and values.ndim == 1 and values.dtype.kind in 'iuf':
        if values.size > 0:
            output = defaultdict()
            output["count"] = values.size
            output["mean"] = values.mean()
            output["min"] = values.min()
            output["max"] = values.max()
            return output
        else:
            raise ValueError
    else:
        raise TypeError


"""
Reflection

1.  What guarantees does your function provide?
The function provides a clear Input and Output contracts. 
 
2.  Which assumptions are explicit?
There are no assumptions in the function. 

3.  Which boundary conditions were dangerous when unspecified?
The data types need to be clearly defined and the type of arrays that the function can take as input should also be 
defined. 

4.  Why should validation be deliberate?
When validations are not deliberately added into the function there can be some run time errors for unvalidated cases. 

5.  What would make this function safer for another engineer to use?
The explicit contracts defined and all the conditions checked make sure that the function is safe to use. 

The exercise done yesterday is similar to the one today, however I have realised that setting up the contracts is so 
important. More important than that is to simplify the functionality of the function being defined. When there is more 
being done in the function then the contracts become complex. Keep it Simple and Stupid is the best policy
"""
