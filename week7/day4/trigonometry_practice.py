import math
import numpy as np

"""
## Drill

Prediction:

np.sin(0)           -> 0
np.cos(0)           -> 1
np.sin(np.pi / 2)   -> 1
np.cos(np.pi)       -> -1

"""

print(np.sin(0))
print(np.cos(0))
print(np.sin(np.pi / 2))
print(np.cos(np.pi * 2/3))

"""
Periodic behaviour
"""

for factor in np.arange(-2, 3.5, 1/6):
    rad = np.pi * factor
    deg = math.ceil(np.rad2deg(rad))
    print(f"sin({deg}):{round(np.sin(rad), 2)}, cos({deg}):{round(np.cos(rad),2)}, tan({deg}):{round(np.tan(rad),2)}")

"""
Imagine a circle with unit radius drawn on a 2D plane with centre as origin on a x and y axis. As we move along the 
circle starting from x = 1 and y = 0 in a counter clockwise direction, the phase increases from 0 to 180/np.pi till we 
reach (-1, 0) in this phase we have positive sin theta i.e, positive imaginary component. As we continue on that circle
to the start the phase increases from 180/np.pi to 360/ 2*np.pi. In this phase the sin theta is negative i,e, the 
imaginary component is negative.

sin theta start from 0 at the starting point and goes up to 1 when as the phase reaches np.pi/2. 
It then decreases back to 0 when we reach np.pi. It can be visualised as the distance from x axis to the point. 

Similarly for the real component we use cos theta. This can be visualised as the distance from y axis to the point.
"""


def unit_complex_from_phase(theta):
    """
    Return the complex number for the given theta. Invalid input returns complex(0, 0)
    :param theta: float
    :return: complex
    """
    try:
        rad = float(theta)
        if not math.isfinite(rad):
            return complex(0, 0)
        real = math.cos(rad)
        imag = math.sin(rad)
        return complex(real,imag)
    except (ValueError, TypeError):
        return complex(0, 0)


"""
Reflection:

1.  Why does a phase angle produce a complex number?
A phase angle determines the position of the point from the origin is in two directions, the distance from the x axis 
is the imaginary part. 

2.  Why is the magnitude of `cos(θ) + i sin(θ)` equal to 1?
cos or sin of a phase is the ratio of the distance from the axis to the origin and according to pythagorus theoram the
sum of the squares of the two sides is equal to the square of the hypotnuse. cos theta is adj/hyp and sin theta is 
opp/hyp. 

Magnitude is sqrt(real^2 + imag^2) i.e, sqrt(cos^2 + sin^2)

3.  Why is explicit documentation of radians important?
radians is the unit of measure in trigonometry and is critical is computations for quantum bits.
"""
