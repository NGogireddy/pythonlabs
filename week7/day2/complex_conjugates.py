import numpy as np

"""
## Drill

values = np.array([
    1 + 2j,
    3 - 4j,
    2 + 0j,
])

Prediction:

values.real             --> np.array([1, 3, 2])
values.imag             --> np.array([2, -4, 0])
np.abs(values)          --> np.array([sqrt(5), 5, 2])
np.conjugate(values)    --> np.array([1 - 2j, 3 + 4j, 2 - 0j])

All predictions are correct. 

"""

values = np.array([
    1 + 2j,
    3 - 4j,
    2 + 0j,
])

print(values.real)
print(values.imag)
print(np.abs(values))
print(np.conjugate(values))
print(values.dtype)


def conjugate_vectors(values):
    """
    Takes a 1D np array of dtype complex and returns its conjugates in np array. Empty array raises TypeError
    :param values:
    :return:
    """
    if isinstance(values, np.ndarray) and values.dtype == 'complex128' and values.ndim == 1 and values.size > 0:
        return np.conjugate(values)
    else:
        raise TypeError


"""
Reflection:

1.  What does conjugation do?
Conjugate inverses the dimension of the imaginary number i.e, it changes the direction of the vector. 

2.  Does conjugation change the shape?
No, conjugate will not change the shape of the vector. 

3.  Why might complex vectors require different handling from ordinary real vectors?
The dtype of complex numbers is carrying an imaginary component in it which works differently from the real numbers and
hence the handling will be different from real vectors. 

"""
