import numpy as np

"""
z = 1 + 1j

Predict its phase: It is 45 deg in angle or pi/4 in radians. pi radians == 180 degrees

np.angle(z)  --> 0.78...
"""

z = 1 + 1j
print(np.angle(z))

a = np.empty(4, dtype=complex)
print(a)
print(np.angle(a))

arr = np.array([1 + 0j, 1 + 1j, 0 + 1j, -1 + 1j, -1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j])
print(np.angle(arr))

"""
## Learn
-   angle / phase  -> if we plot the complex number on a 2D plane it is the angle at which it is located from the origin
It starts with 0 on positive x axis and goes up to pi (3.14) on to the negative x axis in a counter clockwise direction.
If we move in a clockwise direction from +ve X axis to -ve X axis, then the values will be negative. 
 
-   radians     -> Angle measured with respect to pi (3.14).
-   degrees     -> Angle measured in degrees.
-   `np.angle`  -> Angle measured in radians.
-   `np.real`   -> The real part in complex number
-   `np.imag`   -> The imaginary part in complex number
-   relationship between Cartesian form and polar form  -> These are two different forms of representing a complex 
number. Cartesian form is in the a + ib form where we have real and imaginary components and polar form is representing
the complex number using the magnitude and angle i.e distance and direction of the point from origin. The polar form is
r(cos 0 + i sin 0)

"""


def complex_phase(value):
    """
    returns the phase value in degrees for a complex number
    :param value: complex number
    :return: float
    """
    if isinstance(value, complex):
        return np.degrees(np.angle(value))
    else:
        raise TypeError


"""
## Reflection

1.  What is phase?
It gives the angle at which the complex number is. 

2.  Why does NumPy return radians?
radians is the most commonly used measurement in trignometry, calculus and natural calculations. 

3.  What information does magnitude give that phase does not?
The distance from origin. 

4.  What information does phase give that magnitude does not?
The angle at which the complex number is present. 

"""