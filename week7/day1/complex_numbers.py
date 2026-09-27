"""
Drill

z = 3 + 4j

Prediction: 
z.real      -> 3
z.imag      -> 4
abs(z)      -> 5

z + 2       -> 5 + 4j
z * 2       -> 6 + 8j
z * (1 + 1j) -> 7 + 7j  (This is incorrect --> 4j * 1j = -4 not +4)

"""

z = 3 + 4j

print(z.real)
print(z.imag)
print(abs(z))

print(z+2)
print(z*2)
print(z * (1 + 1j))

print(type(z))
print(z.conjugate())


def complex_magnitude(value):
    """
    Return the magnitude of the complex number.
    :param value: complex number
    :return: magnitude
    """
    if isinstance(value, complex):
        return abs(value)
    raise ValueError


"""
Reflection: I can understand the concept of real and imaginary numbers in terms of mathematics, but not able to relate
with real time usage or rather connect it to the quantum computing. I believe I need to wait to link the relation of 
complex numbers to quantum computing. 

1.  What are the real and imaginary parts?
2.  What does magnitude represent?
3.  How is magnitude related to the Week 6 vector norm?

"""
