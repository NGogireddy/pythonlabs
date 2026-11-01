import numpy as np

X = np.array([
    [0, 1],
    [1, 0]
])

Z = np.array([
    [1,  0],
    [0, -1]
])

H = (1 / np.sqrt(2)) * np.array([
    [1,  1],
    [1, -1]
])

state_zero = np.array([1, 0])


def apply_gate(gate, state):
    return gate @ state


after_h = apply_gate(H, state_zero)
after_z = apply_gate(Z, after_h)

print("after_h : ", after_h)
print("after_z : ", after_z)
print("")


def get_probabilities(state):
    return np.abs(state) ** 2


def is_normalized(state):
    return np.isclose(np.sum(get_probabilities(state)), 1)


zero_probability = get_probabilities(state_zero)
after_h_probability = get_probabilities(after_h)
after_z_probability = get_probabilities(after_z)

print(zero_probability)
print(after_h_probability)
print(after_z_probability)
print("")

print("Is state zero normalized : ", is_normalized(state_zero))
print("Is after_h normalized : ", is_normalized(after_h))
print("Is after_z normalized : ", is_normalized(after_z))

state_a = np.array([1, 1])

state_a_probability = get_probabilities(state_a)
print("")
print(state_a_probability)
print("Is state_a normalized : ", is_normalized(state_a))

assert np.allclose(apply_gate(X, state_zero), [0, 1])

assert np.allclose(apply_gate(H, state_zero),
                   [1 / np.sqrt(2), 1 / np.sqrt(2)])

assert np.allclose(apply_gate(Z, after_h),
                   [1 / np.sqrt(2), -1 / np.sqrt(2)])

assert is_normalized(state_zero)
assert is_normalized(after_h)
assert is_normalized(after_z)
assert not is_normalized(state_a)

print("All tests passed!")

after_zh = apply_gate(Z, after_h)
after_hzh = apply_gate(H, after_zh)
print("after first H : ", after_h)
print("after z and h : ", after_zh)
print("after H, Z, H : ", after_hzh)
print("Final measurement probabilities : ", get_probabilities(after_hzh))
