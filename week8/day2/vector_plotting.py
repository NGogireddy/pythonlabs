import numpy as np
import matplotlib.pyplot as plt


arr = np.array([[3, 4]])
# plt.arrow(x=8, y=8, dx=1, dy=1)
# plt.show()

def vector_plotting_using_quiver():
    # Define the vector components [X_component, Y_component]
    vector = [3, 4]

    # Define the starting point (origin)
    origin_x = 0
    origin_y = 0

    # Create the figure and plot the vector
    plt.figure(figsize=(5, 5))

    # plt.quiver arguments:
    # 1 & 2: Start coordinates (origin_x, origin_y)
    # 3 & 4: Vector directions (vector[0], vector[1])
    # angles & scale_units='xy' and scale=1 ensure the vector scales accurately to the axes grid values
    plt.quiver(origin_x, origin_y, vector[0], vector[1],
               angles='xy', scale_units='xy', scale=1, color='blue', label='Vector [3, 4]')

    # Set axis limits with extra padding to see the arrow clearly
    plt.xlim(-1, 5)
    plt.ylim(-1, 5)

    # Add grid lines, labels, a legend, and an origin reference line
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Plotting a 2D Vector')
    plt.legend()

    # Display the plot
    plt.show()


def vector_plotting_using_arrow():
    # Create a blank plot area
    plt.figure(figsize=(6, 6))

    # Plot a basic arrow starting at (0, 0) and extending 3 units right, 4 units up
    plt.arrow(x=0, y=0, dx=3, dy=4,
              width=0.08,          # Thickness of the arrow shaft
              head_width=0.3,      # Width of the arrow head
              head_length=0.4,     # Length of the arrow head
              color='crimson',     # Color of the arrow
              length_includes_head=True) # Forces total length (including head) to equal dx/dy

    # Set plot boundaries so the arrow is fully visible
    plt.xlim(-1, 6)
    plt.ylim(-1, 6)
    plt.grid(True, linestyle=':')

    plt.title("Using plt.arrow()")
    plt.show()


def vector_plotting_using_annotate():

    # Define vector components
    dx, dy = 3, 4

    # Calculate Magnitude and Phase (Angle)
    magnitude = np.sqrt(dx ** 2 + dy ** 2)
    phase_deg = np.arctan2(dy, dx)

    # Set up the plot
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    # 1. Plot the main vector arrow
    plt.quiver(0, 0, dx, dy, angles='xy', scale_units='xy', scale=1, color='blue')

    # 2. Use plt.annotate to point directly at the vector's tip
    plt.annotate(
        f'Vector (dx={dx}, dy={dy})\nMagnitude = {magnitude:.1f}\nPhase = {phase_deg:.3f}°',
        xy=(dx, dy),  # Arrow tip points here (the vector head)
        xytext=(dx - 1.5, dy + 0.5),  # Location where the text block sits
        arrowprops=dict(  # Settings for the annotation line/arrow
            facecolor='black',
            arrowstyle="->",
            connectionstyle="arc3,rad=.2"  # Curved arrow for a polished look
        ),
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3)  # Background bubble
    )

    # 3. Use plt.annotate WITHOUT an arrow to mark the Phase Angle near the origin
    # Setting xytext=None ensures the string sits directly at the 'xy' coordinate
    plt.annotate(
        f"θ = {phase_deg:.5f}°",
        xy=(0.5, 0.4),  # Text placement near the angle vertex
        color='darkgreen',
        weight='bold'
    )

    # Cosmetic formatting
    plt.xlim(-1, 5)
    plt.ylim(-1, 6)
    plt.grid(True, linestyle=':')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Vector Annotation with Magnitude & Phase')

    plt.show()


def plotting_multiple_vectors_in_one_graph(vectors=np.empty((0, 2))):
    # Sample input array of vectors: [[dx1, dy1], [dx2, dy2], ...]
    if vectors.size == 0:
        vectors = np.array([[3, 4], [-3, -4], [-2, 5], [5, 2]])

    # Extract all X components (first column) and Y components (second column)
    dx_components = vectors[:, 0]
    dy_components = vectors[:, 1]

    # Define starting points for all vectors.
    # Setting them to 0 tells Matplotlib every vector starts at the origin (0, 0)
    origins_x = np.zeros(len(vectors))
    origins_y = np.zeros(len(vectors))

    # Create the plot area
    plt.figure(figsize=(7, 7))

    # Plot all vectors at once
    # We pass a list of colors so each vector is easily distinguishable
    colors = ['blue', 'crimson', 'forestgreen', 'darkorange']
    plt.quiver(origins_x, origins_y, dx_components, dy_components,
               angles='xy', scale_units='xy', scale=1, color=colors)

    # Set axis limits dynamically based on the largest vector coordinates (plus padding)
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)

    # Add baseline grid structure
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle='--')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Plotting Multiple Vectors from the Origin')

    plt.show()


if __name__ == "__main()__()":
    plotting_multiple_vectors_in_one_graph()

"""
## Reflection

In this world of AI, I am able to easily do a google search and get code to plot the vectors. I am not able to gain 
muscle memory of these commands as there are various parameters to pass for the quiver() or arrow() or annotate(). 
Should I gain muscle memory of these functions or understand the concept and proceed?  

I am not doing a test today as it is similar to yesterday. My understanding today is about how to plot the vectors in a 
graph. The basic fundamental here is to pass the x,y co-ordinates of the starting point and the displacement of x and y 
for the vector. This will plot the vector from x,y to (x+dx, y+dy). If we want multiple vectors in the same graph, we 
need to pass the x co-ordinates in an array, y co-ordinates in another array. Similarly dx and dy values as well. 
First vector will be plotted for the values in index 0, second vector will be plotted for the values in index 1 and 
so on. 

Explain:

> How does the visual length of a vector relate to the norm you learned in Week 6?
norm is nothing but the distance of the vector point from the origin which is the visual length of the vector. They 
both are same. 

"""