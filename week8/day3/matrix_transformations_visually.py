import numpy as np
import matplotlib.pyplot as plt

"""
## Drill

Use a simple transformation matrix:

A = [[2, 0],
     [0, 1]]
and a vector:

v = [1, 1]

Calculate:

A @ v   ==>     [2, 1] 

Predict what happened geometrically: The first row transformed the dimension of the vector on the first axis, second 
one transformed it on y axis. This happened as the y component is '0' in first row and x is '0' in the second row. 

A = [[-1, 0],
     [0, 1]]

Will flip the vector on X axis. 

A = [[-1, 0],
     [0, -1]]

Will flip the vector on both X and Y axis. 

A = [[1, 0],
     [0, 1]]

The identity matrix will not transform the vector. 

A = [[n, 0],
     [0, n]]

This will increase the magnitude of the vector by 'n', keeps the phase constant.  

The phase changes when the y component in the first row and/or x component in the second row have non zero values.
"""

def plot_transformation_vectors(mat=np.array([[1, 0], [0, 1]]), vec=np.empty([0, 2])):
    """
    Plots original vector and the transformed vector in the same graph
    :param mat: a 2 X 2 numpy array of dtype in 'iuf'
    :param vec: an array of 2d numpy vectors
    :return: None
    """
    if isinstance(mat, np.ndarray) and mat.shape == (2, 2) and mat.dtype.kind in 'iuf':
        if isinstance(vec, np.ndarray) and mat.dtype.kind in 'iuf':
            transformed_vec = (mat @ vec.T).T
            print(f'Original vectors: {vec}')
            print(f'Transformed vectors: {transformed_vec}')

            plt.axhline(0, color='black', linewidth=0.8)
            plt.axvline(0, color='black', linewidth=0.8)

            origins_x = np.zeros(len(vec))
            origins_y = np.zeros(len(vec))

            # Plot the vectors starting from the origin (0, 0)
            # Original vector (Blue)
            plt.quiver(origins_x, origins_y, vec[:, 0], vec[:, 1], angles='xy', scale_units='xy', scale=1,
                       color='royalblue', label='Original Vector')

            # Transformed vector (Crimson)
            plt.quiver(origins_x, origins_y, transformed_vec[:, 0], transformed_vec[:, 1], angles='xy',
                       scale_units='xy', scale=1, color='crimson', label=f'Transformed Vector')

            # Axis formatting
            neg_x = min(min(vec[:, 0]), min(transformed_vec[:, 0]))
            neg_y = min(min(vec[:, 1]), min(transformed_vec[:, 1]))
            pos_x = max(max(vec[:, 0]), max(transformed_vec[:, 0]))
            pos_y = max(max(vec[:, 1]), max(transformed_vec[:, 1]))
            plt.xlim(neg_x-1, pos_x+1)
            plt.ylim(neg_y-1, pos_y+1)
            plt.grid(True, linestyle=':', alpha=0.6)
            plt.xlabel('X Axis')
            plt.ylabel('Y Axis')
            plt.title('Real-World Matrix Transformation')
            plt.legend(loc='upper right')
            plt.gca().set_aspect('equal') # Forces pixels to be perfectly square so geometry looks correct

            plt.show()


plot_transformation_vectors(np.array([[0.5, 0], [0, -0.5]]), np.array([[1, -2], [-2, -1]]))

"""
## Reflection

Explain: What does the matrix do to a vector geometrically?

I was fascinated to see what happens to a vector when transformation is done to it using a transformation matrix. Whilst
studying about transformation, I have understood the use of transformation in real life. 

Eg: Rotation/Reflection of images can be done using matrices.

When transformation is applied stretching and shearing happens to the original plane and hence the vector gets 
transformed as well.   

When a transformation is done using a matrix [[x1, y1][x2, y2]]. On X axis a stretch by x1 units and shear by x2 units
will happen. Similarly on y axis a stretch by y2 units and shear by y1 units happen simultaneously on both the axes. 

The best examples of real life applications are image processing, creating italicized fonts, autonomous cars image 
processing whilst turning etc. 

PS: Test cases are not written for this day as well. If needed, I will revisit and do them in another week.  

"""
