import numpy as np


"""
## Drill

Start with:

A = [[2, 0],
     [0, 3]]

Try to find vectors whose direction does not change when multiplied by `A`.

[1, 0] [0, 1] are the two eigen vectors for this matrix. 

> What changed when the transformation is applied?
The plane has stretched in both the directions. Two times on the x axis and 3 times on the y axis. 
The vector [1 0] gets transformed into [2 0]. The Eigen value is 2 and the vector is [1 0]. Similarly
for [0 3] the eigen values is 3 and vector is [0 1].

The eigenvalue tells how the eigenvector is scaled. In this example for the eigen vector [1 0] the eigen
value 2 says that the original vector is scaled twice once transformed. 

"""

def get_eigen_values(mat=np.array([[1, 0], [0, 1]])):
    """
    Returns a list os eigen values and eigen vectors as two individual arrays
    :param mat: numpy matrix where the last two dimensions are same for generating Eigen Values
    :return: EigenResult if valid input otherwise None.
    """
    if isinstance(mat, np.ndarray) and mat.ndim > 1 and mat.size > 0 and mat.dtype.kind in 'iuf':
        mat_shape = mat.shape
        if mat_shape[-1] == mat_shape[-2]:
            eig_value = np.linalg.eig(mat)
            return eig_value
    return None


A = np.array([[[[1, 2], [4, 5]],
               [[2, 3], [8, 9]],
               ],
              [[[1, 2], [4, 5]],
               [[2, 3], [8, 9]],
               ],
              ])
eig_value = np.linalg.eig(A)
print(A.ndim)
print(eig_value)
print(type(eig_value))

