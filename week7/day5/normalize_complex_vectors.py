import numpy as np
import math

"""
Designing the contract for the function normalise_complex_vector(values)

-   input shape
This function takes 1D complex vectors as input. Any 1D vectors of other dtypes will raise TypeError exception. Limiting
the scope of this function to only 1 dimension. Any complex vectors of 2 or more dimensions will also raise TypeError. 
 
-   dtype
The only valid dtype of the vector is complex. Plain integers or floating point numbers are subset of complex numbers, 
however normalising them will return 1 for every element, hence these input types are not valid in this scope.   

-   empty input
If the input is an empty 1D vector of dtype complex then it will raise TypeError.  

-   output type
Output is a 1D np array of dtype complex numbers. 

-   what "normalise" means

-   what happens when the vector has zero magnitude
For a vector having zero magnitude, returns the same vector. 

-   whether the original array is modified
Original array is not modified. 

-   what exceptions are appropriate
To limit the scope, any invalid inputs raise TypeError. 

"""


def normalized_vector(values):
    """
    Returns the normalized vector for the input vector
    :param values: 1D np array of complex vectors
    :return: 1D np array of complex vectors
    """
    if isinstance(values, np.ndarray) and values.dtype == 'complex128' and values.ndim == 1 and values.size > 0:
        sum = 0
        for value in values:
            sum += abs(value)**2
        if sum == 0:
            return values
        else:
            return values/math.sqrt(sum)
    else:
        raise TypeError


def normalize_vector(values):
    """
    A better implementation of previous function
    :param values: 1D np array of complex vectors
    :return: 1D np array of complex vectors
    """
    if isinstance(values, np.ndarray) and values.dtype == 'complex128' and values.ndim == 1 and values.size > 0:
        # 1. Calculate the L2 norm (magnitude)
        norm = np.linalg.norm(values)

        # 2. Divide to get the unit vector (safely checking for zero vectors)
        v_normalized = values / norm if norm > 0 else values

        return v_normalized
    else:
        raise TypeError


"""
## Reflection

1.  Why can a zero vector not be normalised?
To normalize a vector we need to divide the vector by the norm of the vector, for zero vector the norm is zero and 
division by zero is not possible. 

2.  Why is `assert_allclose` more appropriate than exact equality?
When we normalize the vector divisions happen and the results will be floating point. Normal Assertions may not work 
with floating point numbers. 

3.  What contract decision did you make about empty vectors?
We can't normalize an empty vector hence raised TypeError. 

4.  What contract decision did you make about mutation?
The original vector should remains untouched i.e, no mutation allowed on the input values.  

"""