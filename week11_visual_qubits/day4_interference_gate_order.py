import numpy as np

X = np.array([[0, 1],
              [1, 0]])

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

plus = (1 / np.sqrt(2)) * np.array([1, 1])
minus = (1 / np.sqrt(2)) * np.array([1, -1])

print("X|+>:", X @ plus)
print("X|->:", X @ minus)

print("H(X|+>):", H @ (X @ plus))
print("H(X|->):", H @ (X @ minus))
