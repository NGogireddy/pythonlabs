import numpy as np
import matplotlib.pyplot as plt

"""
A small numerical visualisation program that:

1.  Creates a 2D transformation matrix
2.  Defines a small set of 2D vectors
3.  Transforms the vectors using matrix multiplication
4.  Calculates the matrix's eigenvalues/eigenvectors
5.  Identifies the eigenvectors among the visualised directions where
    appropriate
6.  Plots the original and transformed vectors
7.  Provides a concise numerical summary
"""

"""
Input: Create a random 2 X 2 numpy matrix, Creates 2 2D vectors. 
  ↓
Validation: Validates that the matrix is deterministic. 
  ↓
Transformation: Transforms the two 2D vectors using the transformation matrix generated. 
  ↓
Eigen-analysis: Calculate the Eigen Values and Eigen Vectors. 
  ↓
Visualisation: Use matplotlib.pyplot to plot the vectors before and after transformation. 
  ↓
Summary: Print a summary of the vectors before and after transformation. 
"""


def generate_transformation_matrix(n=2):
    if isinstance(n, int) and n >= 2:
        return np.random.rand(n, n)
    raise ValueError


def generate_n_sample_vectors(n=2, m=2):
    """
    :param n: Number of sample vectors needed
    :param m: number of dimensions in each vector
    :return:
    """
    if isinstance(n, int) and isinstance(m, int) and n>=2 and m>=2:
        return np.random.rand(n, m)
    raise ValueError


def is_valid_transformation_matrix(mat):
    """
    Validates if the matrix is deterministic
    :param mat:
    :return:
    """
    return not (np.linalg.det(mat) == 0)


def is_transformation_possible(matrix, vectors):
    return matrix.shape[0] == vectors.shape[1]


def transform_vectors(mat, vectors):
    """
    Using the transformation matrix mat, transform the vectors and return them.
    :param mat:
    :param vectors:
    :return:
    """
    return (mat @ vectors.T).T


def get_eigen_values_and_vectors(mat):
    return np.linalg.eig(mat)


def plot_vectors(orig, transformed):
    """
    Plots the original vectors in blue and transformed vectors in red
    :param orig:
    :param transformed:
    :return:
    """
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    origins_x = np.zeros(len(orig))
    origins_y = np.zeros(len(orig))

    # Plot the vectors starting from the origin (0, 0)
    # Original vector (Blue)
    plt.quiver(origins_x, origins_y, orig[:, 0], orig[:, 1], angles='xy', scale_units='xy', scale=1,
               color='royalblue', label='Original Vector')

    # Transformed vector (Crimson)
    plt.quiver(origins_x, origins_y, transformed[:, 0], transformed[:, 1], angles='xy',
               scale_units='xy', scale=1, color='crimson', label=f'Transformed Vector')

    # Axis formatting
    neg_x = min(min(orig[:, 0]), min(transformed[:, 0]))
    neg_y = min(min(orig[:, 1]), min(transformed[:, 1]))
    pos_x = max(max(orig[:, 0]), max(transformed[:, 0]))
    pos_y = max(max(orig[:, 1]), max(transformed[:, 1]))
    plt.xlim(neg_x - 0.2, pos_x + 0.2)
    plt.ylim(neg_y - 0.2, pos_y + 0.2)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Real-World Matrix Transformation')
    plt.legend(loc='upper right')
    plt.gca().set_aspect('equal')  # Forces pixels to be perfectly square so geometry looks correct

    plt.show()


def simulation_steps():
    matrix = generate_transformation_matrix()
    if is_valid_transformation_matrix(matrix):
        vectors = generate_n_sample_vectors(3, 2)
        print("Transformation Matrix is : ")
        print(matrix)
        print("Original vectors are : ")
        print(vectors)
        if is_transformation_possible(matrix, vectors):
            transformed_vectors = transform_vectors(matrix, vectors)
            print("Transformed vectors are : ")
            print(transformed_vectors)
            eig_values, eig_vectors = get_eigen_values_and_vectors(matrix)
            print("Eigen values : ")
            print(eig_values)
            print("Eigen vectors : ")
            print(eig_vectors)
            plot_vectors(vectors, transformed_vectors)


if __name__ == '__main__':
    simulation_steps()

"""
Reflection: 
On Day6 the code is done with barebones i.e, to work with default matrix of 2*2. On Day7, the code has been modified to 
add a parameter for the shape of the matrix i.e, should it be 3*3 or 4*4. The validations and exceptions raised are all
done on Day7. 

The final project will do all the calculations properly, but the plot has not been adjusted due to time constraint. 
More over plotting a graph for any matrix of shape 4*4 and beyond is not realistic. The above plotting code should work 
for a 2*2 matrix. 
"""