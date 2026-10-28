def apply_hadamard_to_bloch(coords):
    """Return the Bloch coordinates after a Hadamard gate.
    coords is a tuple with only x, y, z coordinates on a bloch sphere
    """
    x, y, z = coords
    return z, -y, x


states = [
    (0, 0, 1),   # |0>
    (1, 0, 0),   # |+>
    (0, 1, 0),   # +Y
    (0, 0, -1),  # |1>
]

for state in states:
    once = apply_hadamard_to_bloch(state)
    twice = apply_hadamard_to_bloch(once)

    assert twice == state
    print(f"{state} -> {once} -> {twice}")

"""
Learning: 
Hadamard gate is switching the x and z axis and reversing the y axis. 
Pauli X is rotating the block sphere on X axis
Pauli Z is rotating the block sphere on Z axis
"""
