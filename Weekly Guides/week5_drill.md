# Quantum Learning Blueprint: Week 5
## Topic: NumPy Foundations — Linear Algebra & Complex Vector Spaces

### Week 5 Blueprint Overview
This week bridges foundational Python data structures with high-performance numerical computing. You will transition from list-based logic to memory-aligned NumPy operations, focusing heavily on the linear algebra and complex number primitives required for quantum computing (state vectors and unitary operators).

---

## Day 1: Array Mechanics, Memory Views, and Copies
* **Focus:** Transition from nested Python lists to contiguous NumPy memory. Understanding views vs. copies to prevent subtle pointer mutation bugs.
* **Max Time:** 60 minutes

### 1. Learn (15 mins)
* Fixed-type contiguous memory allocation vs. Python object arrays.
* Visualising array metadata: `.shape`, `.strides`, `.dtype`, and memory flags.
* Memory management: The difference between a structural **view** (`.view()`, basic slicing) and a deep **copy** (`.copy()`, advanced indexing).

### 2. Drill & Implement (25 mins)
Implement a utility function that safely clones or views an array while verifying memory location safety.

```python
import numpy as np

def manipulate_array_memory(arr: np.ndarray, structural_change: bool) -> np.ndarray:
    """
    Modifies or returns a structural representation of an input array based on safety flags.
    
    CONTRACT:
    - Input:
        - arr: A non-empty, contiguous 1D or 2D np.ndarray.
        - structural_change: bool. If True, returns a shallow memory view with a modified shape.
                             If False, returns a completely isolated deep copy.
    - Output: Returns a np.ndarray.
    - Invalid Input / Exceptions:
        - Raises TypeError if arr is not an instance of np.ndarray.
        - Raises ValueError if arr is empty (size == 0).
    - Side-Effects: None. Modifying the output of a deep copy must not mutate the original `arr`.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a valid NumPy ndarray.")
    if arr.size == 0:
        raise ValueError("Cannot process an empty array.")
        
    if structural_change:
        # Return a view flattened if 2D, or expanded if 1D
        return arr.view()
    return arr.copy()
```

### 3. Test (15 mins)
Write a strict test suite validating memory sharing using `np.shares_memory()`.

```python
import pytest
import numpy as np

@pytest.mark.parametrize("shape, structural_change, expected_share", [
    ((4,), True, True),
    ((2, 2), False, False),
])
def test_array_memory_isolation(shape, structural_change, expected_share):
    original = np.arange(np.prod(shape)).reshape(shape)
    result = manipulate_array_memory(original, structural_change)
    
    assert np.shares_memory(original, result) == expected_share
    
    # Mutate result to confirm contract side-effect profile
    result.fill(99)
    if not expected_share:
        assert not np.all(original == 99)

def test_array_memory_exceptions():
    with pytest.raises(TypeError):
        manipulate_array_memory([], False)
    with pytest.raises(ValueError):
        manipulate_array_memory(np.array([]), False)
```

### 4. Reflection (5 mins)
* Why does a basic slice (e.g., `arr[:2]`) create a view rather than a copy? How can this lead to memory leaks or data corruption if unmanaged?

---

## Day 2: Vector Spaces, Dot Products, and Custom Exceptions
* **Focus:** Vector geometry, projection operations, and handling invalid dimensional match properties with explicit custom error trees.
* **Max Time:** 60 minutes

### 1. Learn (15 mins)
* Coordinate spaces, vector dimensions, and inner products <ψ|φ>.
* `np.dot` vs. `np.inner` vs. the `@` operator.
* Vector projection mechanics and numerical scale bounds.

### 2. Drill & Implement (25 mins)
Implement a strict geometric vector projecting function.

```python
import numpy as np

class DimensionalityMismatchError(ValueError):
    """Raised when spatial dimensions do not align for algebraic operations."""

def project_vector(v: np.ndarray, u: np.ndarray) -> np.ndarray:
    """
    Projects vector v onto vector u.
    
    CONTRACT:
    - Input:
        - v: 1D real-valued float np.ndarray representing the vector to project.
        - u: 1D real-valued float np.ndarray representing the target basis vector.
    - Output: A 1D float np.ndarray representing the projection component.
    - Invalid Input / Exceptions:
        - Raises DimensionalityMismatchError if v.shape != u.shape.
        - Raises ZeroDivisionError if u is a zero vector (norm is 0).
    - Side-Effects: None.
    """
    if v.ndim != 1 or u.ndim != 1:
        raise ValueError("Vectors must be 1-dimensional.")
    if v.shape != u.shape:
        raise DimensionalityMismatchError(f"Shape mismatch: {v.shape} vs {u.shape}")
        
    u_norm_sq = np.dot(u, u)
    if np.isclose(u_norm_sq, 0.0, atol=1e-15):
        raise ZeroDivisionError("Cannot project onto a zero-magnitude vector.")
        
    return (np.dot(v, u) / u_norm_sq) * u
```

### 3. Test (15 mins)
Use `pytest.approx` or `np.testing` variants to assert float alignments.

```python
import pytest
import numpy as np

def test_projection_orthogonal():
    v = np.array([1.0, 0.0])
    u = np.array([0.0, 1.0])
    result = project_vector(v, u)
    np.testing.assert_allclose(result, [0.0, 0.0], atol=1e-15)

def test_projection_errors():
    with pytest.raises(DimensionalityMismatchError):
        project_vector(np.array([1.0, 2.0]), np.array([1.0]))
        
    with pytest.raises(ZeroDivisionError):
        project_vector(np.array([1.0, 2.0]), np.array([0.0, 0.0]))
```

### 4. Reflection (5 mins)
* Why should you never use raw equality operators (`==`) when testing floating-point array products? What does `atol` vs `rtol` signify?

---

## Day 3: Matrices as Linear Transformations
* **Focus:** Matrix transformations, dimensional mapping, and checking matrix attributes (invertibility, rank).
* **Max Time:** 60 minutes

### 1. Learn (15 mins)
* Linear maps, transformation matrices, and composition via matrix multiplication.
* Matrix rank, determinants, and properties of invertibility (`np.linalg.det`, `np.linalg.matrix_rank`).
* Broad-scale performance effects of multi-matrix chained dot products (`np.linalg.multi_dot`).

### 2. Drill & Implement (25 mins)

```python
import numpy as np

def apply_linear_transform(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """
    Applies a square matrix linear transformation to a given vector spatial point.
    
    CONTRACT:
    - Input:
        - matrix: 2D square float np.ndarray of shape (N, N).
        - vector: 1D float np.ndarray of shape (N,).
    - Output: 1D float np.ndarray of shape (N,).
    - Invalid Input / Exceptions:
        - Raises ValueError if matrix is not 2D square or vector shape does not match.
        - Raises LinAlgError if the matrix is singular (rank < N).
    - Side-Effects: None.
    """
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Transformation matrix must be 2D and square.")
    if vector.ndim != 1 or matrix.shape[1] != vector.shape[0]:
        raise ValueError("Vector dimension must match matrix column count.")
        
    rank = np.linalg.matrix_rank(matrix)
    if rank < matrix.shape[0]:
        raise np.linalg.LinAlgError("Transformation matrix is singular; configuration loses rank.")
        
    return matrix @ vector
```

### 3. Test (15 mins)

```python
import pytest
import numpy as np

def test_valid_transform():
    matrix = np.array([[2.0, 0.0], [0.0, 3.0]])
    vector = np.array([1.0, 1.0])
    expected = np.array([2.0, 3.0])
    np.testing.assert_array_equal(apply_linear_transform(matrix, vector), expected)

def test_singular_matrix_throws():
    singular_matrix = np.array([[1.0, 2.0], [2.0, 4.0]]) # Linearly dependent rows
    vector = np.array([1.0, 2.0])
    with pytest.raises(np.linalg.LinAlgError):
        apply_linear_transform(singular_matrix, vector)
```

### 4. Reflection (5 mins)
* What is the computational complexity difference between computing a matrix inverse outright versus resolving transformations via vector-matrix execution chains?

---

## Day 4: Introduction to Complex Spaces & Bra-Ket Notation
* **Focus:** Complex array operations, the Hermitian conjugate (conjugate transpose), and complex magnitude extraction.
* **Max Time:** 60 minutes

### 1. Learn (15 mins)
* Native complex dtypes in NumPy (`np.complex64`, `np.complex128`).
* Accessing real and imaginary parts using `.real` and `.imag`.
* The Hermitian Conjugate (Adjoint operator ✝): A† = (A*)^T. Note: `.T` on complex matrices only transposes; it does *not* conjugate.

### 2. Drill & Implement (25 mins)

```python
import numpy as np

def hermitian_conjugate(matrix: np.ndarray) -> np.ndarray:
    """
    Computes the Hermitian conjugate (adjoint) of a complex-valued matrix.
    
    CONTRACT:
    - Input:
        - matrix: 2D complex or float np.ndarray.
    - Output: 2D complex np.ndarray representing the conjugate transpose.
    - Invalid Input / Exceptions:
        - Raises ValueError if matrix is not 2D.
    - Side-Effects: None.
    """
    if matrix.ndim != 2:
        raise ValueError("Hermitian conjugate requires a 2D matrix.")
    
    # Conjugate elements and transpose structurally
    return matrix.conj().T
```

### 3. Test (15 mins)

```python
import pytest
import numpy as np

@pytest.mark.parametrize("input_matrix, expected_output", [
    (
        np.array([[1+1j, 2-3j], [4j, 5]]), 
        np.array([[1-1j, -4j], [2+3j, 5]])
    ),
])
def test_hermitian_conjugate(input_matrix, expected_output):
    result = hermitian_conjugate(input_matrix)
    np.testing.assert_array_equal(result, expected_output)
```

### 4. Reflection (5 mins)
* Why is a standard `.T` transpose operation insufficient when processing linear operations on complex quantum state amplitudes?

---

## Day 5: Unitary Matrices and State Normalisation
* **Focus:** Verifying preservation of probability amplitudes within quantum states via Unitary operators.
* **Max Time:** 60 minutes

### 1. Learn (15 mins)
* Unitary matrix definitions: U†U = UU† = I.
* Inner products of complex state vectors and preservation of the L2 norm (Σ|c_i|^2 = 1).
* Using `np.eye` to test against standard coordinate identity frames.

### 2. Drill & Implement (25 mins)

```python
import numpy as np

def is_unitary_operator(matrix: np.ndarray, tolerance: float = 1e-12) -> bool:
    """
    Verifies if a complex square matrix behaves as a valid Unitary operator.
    
    CONTRACT:
    - Input:
        - matrix: 2D square complex/float np.ndarray.
        - tolerance: float boundary window evaluating identity differences.
    - Output: bool specifying whether structural criteria matched.
    - Invalid Input / Exceptions:
        - Raises ValueError if matrix properties are asymmetric or non-square.
    - Side-Effects: None.
    """
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Operator must be a 2D square matrix.")
        
    n = matrix.shape[0]
    identity = np.eye(n, dtype=complex)
    
    # Compute U_dagger * U
    adjoint = matrix.conj().T
    product = adjoint @ matrix
    
    return bool(np.allclose(product, identity, atol=tolerance))
```

### 3. Test (15 mins)

```python
import pytest
import numpy as np

def test_unitary_hadamard():
    # 1/sqrt(2) * [[1, 1], [1, -1]]
    hadamard = (1 / np.sqrt(2)) * np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)
    assert is_unitary_operator(hadamard)

def test_non_unitary():
    invalid_matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=complex)
    assert not is_unitary_operator(invalid_matrix)
```

### 4. Reflection (5 mins)
* Why do physical quantum gates need to be strictly unitary? What happens to the probability profile of a state vector if it is multiplied by a non-unitary matrix?

---

## Day 6: Capstone Project — State Vector Simulator Primitives
* **Focus:** Putting it all together. Build a non-prescriptive, modular framework validating execution chains of state vectors processed via quantum operator gates.
* **Max Time:** 60 minutes

### Capstone Requirements
Build a small engine that handles **Quantum State Vector Operations**. 

1. **State Construction & Normalisation**: Accepting arbitrary complex vectors, validating properties, and formatting them into validated complex state configurations with unit probability (||ψ||_2 = 1).
2. **Gate Registration**: Storing known valid transformations (like Pauli-X, Pauli-Z, or Hadamard matrices).
3. **Execution Pipeline**: Applying a sequence of transformations to a state vector while raising precise exceptions if dimensional alignment fails or unitarity is broken.

#### Architectural Constraints (Strictly Enforced)
* No artificial abstractions or forcing of unnecessary design patterns. Keep objects clear, functions modular, and types exact.
* Implement custom error boundaries for domain errors (e.g., `InvalidStateError`, `NonUnitaryOperatorError`).

```python
# Save as quantum_simulator.py (or keep in a local execution scratchpad)
# Implement the internal architectures yourself based on the specifications above.
```

---

## Day 7: Engineering Judgment, Memory Profiles, & Optimization
* **Focus:** Deep evaluation of the Day 6 Capstone system. Focus on performance tracing, precision boundaries, and code refactoring.
* **Max Time:** 60 minutes

### 1. Test Review & Exhaustive Matrix Coverage (20 mins)
Review your test suites from the week. Ensure your capstone has 100% mutation test coverage using complex states. Add comprehensive edge cases for multi-step processing:
* What happens when applying 10 consecutive operations? Does floating-point error accumulate?
* Implement a test tracking identity loop properties (e.g., applying the Pauli-X gate twice should return the exact starting state).

### 2. Memory & Copy Analysis (20 mins)
Profile your pipeline's memory efficiency. Look closely at how arrays are modified using the following code snippets:

```python
# Memory Profile Diagnostic Snippet
import numpy as np
import sys

state = np.array([1.0+0j, 0.0+0j], dtype=np.complex128)
print(f"State base reference pointer share: {state.base}")
print(f"Byte profile tracking size: {state.nbytes} bytes")
```
* Walk through every line of your execution engine. Are you creating new array allocations inside your loop (`matrix @ state` creates a new array allocation each time)? 
* Could you use pre-allocated output buffers (`np.dot(matrix, state, out=buffer_space)`) to optimize execution if this were run millions of times?

### 3. Engineering Judgment Reflection (20 mins)
Document answers to the following system engineering design trade-offs:
* **Precision Trade-off**: When should a simulator choose `np.complex64` (single precision) over `np.complex128` (double precision)? Analyze this from the perspective of cache locality vs. deep circuit floating-point drift.
* **Architecture Critique**: If your simulator needs to scale from 1 qubit to 20 qubits, what happens to memory scaling when using dense matrices? At what point does storing state amplitudes as a dense 1D NumPy array become a structural bottleneck?

---

## Progress Sign-off
* [ ] Day 1 Complete
* [ ] Day 2 Complete
* [ ] Day 3 Complete
* [ ] Day 4 Complete
* [ ] Day 5 Complete
* [ ] Day 6 Capstone Operational
* [ ] Day 7 Memory Profiles and Code Audited
