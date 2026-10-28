import numpy as np

sqrt2 = np.sqrt(2)

H = (1 / sqrt2) * np.array([
    [1,  1],
    [1, -1]
])

plus = np.array([1, 1]) / sqrt2
minus = np.array([1, -1]) / sqrt2

result_plus = H @ plus
result_minus = H @ minus

print("H|+>:", result_plus)
print("Probabilities:", np.abs(result_plus) ** 2)

print("H|->:", result_minus)
print("Probabilities:", np.abs(result_minus) ** 2)

"""
Learning: Applying the gate will not change the state of the qubit. It modifies the amplitudes and takes them close to 
either 0 or 1 based on the probabilities (square of amplitude)

Geometrically Pauli X is 180 degree rotation on X axis i.e, Northern hemisphere becomes Southern and vice versa. State
plus and state minus will not change when X is applied. 

Similarly Pauli Z is 180 degree rotation on Z axis i.e, Eastern hemisphere becomes Western and vice versa. State zero 
and state one will not change when Z is applied. 
"""

""" Here is my understanding of qubit concepts with an analogy. Please give me feedback. 
Bloch sphere as analogy to the globe. 
Imagine the Globe as a bloch sphere. 
    1. North pole is the state zero. 
    2. South pole is the state one. 
    3. Equator and 0 degree longitude (Prime Meridian) meets at Gulf of Guinea and this is state plus.
    4. Equator and 180 degree longitude (Anti meridian) meets at Open waters of Pacific Ocean which would be state minus 
    5. If a vector's state is pointing to Northern hemisphere the probability of measurements resulting in '0' will be 
       more than the result being '1' and vice versa for the vector state in southern hemisphere. 
    6. The phase - angle (phi) is the angle of the vector relative to the Prime Meridian. Change in phase will not 
       impact the measurement probabilities. 
    7. The amplitude - angle (theta) is the angle of the vector relative to the north pole. Change in this angle will 
       impact the amplitude and hence the measurement probabilities. 
    8. State plus and minus are both on the equator and equidistant from both the poles and hence the probabilities of 
       measuring zero and one is 0.5 and 0.5. But the phase of both the states are different. 
    9. Applying Pauli X gate will switch the amplitude of the vector and will inverse the probabilities of measuring 
       0 or 1. In the analogy of globe the vector is moved from Northern Hemisphere to Southern Hemisphere or vice versa
    10. Applying Pauli Z will change only the phase of the vector i.e, in the analogy of globe moves the vector from 
        a location in East to a location in West or vice versa.   
"""
