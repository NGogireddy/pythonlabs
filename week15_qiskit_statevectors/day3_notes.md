### Pauli-Y Gate and Bloch Sphere Rotation

The Pauli-Y gate is the third Pauli operator, alongside Pauli-X and Pauli-Z.

**Pauli-Y matrix:**

```text
Y = [[ 0, -i],
     [ i,  0]]
```

Like X and Z, the Y gate represents a 180-degree rotation around its respective Bloch sphere axis, up to a global phase.

**1. Applying Pauli-Y to |+⟩**

Initial state:

```text
|+> = [1/√2, 1/√2]
```

After applying Y:

```text
Y|+> = [-i/√2, i/√2]
     = -i|-> 
```

Geometrically, a 180-degree rotation around the Y axis takes the positive X direction to the negative X direction. The resulting state is therefore |−⟩ on the Bloch sphere.

The additional factor `-i` is a global phase. It does not change the physical state or its measurement probabilities.

**2. Comparing X and Y on |+⟩**

| Operation | Result |
|---|---|
| X applied to |+⟩ | |+⟩ |
| Y applied to |+⟩ | -i|−⟩ |

Both states produce identical computational-basis measurement probabilities:

```text
After X: [0.5, 0.5]
After Y: [0.5, 0.5]
```

**3. Applying Hadamard after X and Y**

Applying Hadamard reveals the difference between these states:

```text
H(X|+>) = |0>
H(Y|+>) = -i|1>
```

The resulting measurement probabilities are:

```text
After H and X: [1.0, 0.0]
After H and Y: [0.0, 1.0]
```

**Key takeaways:**

- The Bloch sphere represents the physical quantum state but does not display global phase.
- The Pauli-Y gate introduces imaginary amplitudes.
- States can have identical measurement probabilities in one basis but still be physically different.
- A basis transformation can reveal differences that are not visible in the original measurement basis.