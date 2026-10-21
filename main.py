"""
Brody and Zoe
Scientific Computing - Dr. J
Project 3 - Fractal Exploration
10/20/2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


## Koch Snowflake
def koch_snowflake(ax: Axes) -> None:
    """
    Plots the Koch Snowflake fractal onto the provided matplotlib axis.
    
    Uses recursion to generate the geometry
    It uses complex numbers to rotate line segments by 60 degrees.
    
    It starts with an equilateral triangle and repeatedly replaces the middle third of each side with two new segments forming an outward point.

    Args:
        ax (matplotlib.axes.Axes): The subplot axis to draw on
    """

    def koch_curve(p1, p2, depth):
        if depth == 0:
            return [p1]
        
        v = p2 - p1
        pA = p1 + v / 3.0                                  
        pB = pA + (v / 3.0) * np.exp(1j * np.pi / 3.0)     
        pC = p1 + 2.0 * v / 3.0                            
        
        return (koch_curve(p1, pA, depth - 1) +
                koch_curve(pA, pB, depth - 1) +
                koch_curve(pB, pC, depth - 1) +
                koch_curve(pC, p2, depth - 1))

    p1 = 0 + 0j
    p2 = 1 + 0j
    p3 = 0.5 + (np.sqrt(3)/2) * 1j

    depth = 4
    points = (koch_curve(p1, p2, depth) + 
            koch_curve(p2, p3, depth) + 
            koch_curve(p3, p1, depth) + 
            [p1]) 

    x, y = np.real(points), np.imag(points)

    ax.plot(x, y, color='blue', linewidth=1)
    ax.fill(x, y, color='lightblue', alpha=0.5)
    ax.axis('equal') 
    ax.axis('off')   
    ax.set_title(f'Koch Snowflake (Depth {depth})')


## Sierpinski Triangle
def sierpinski_triangle(ax: Axes) -> None:
    """
    This plot uses the Chaos Game algorithm.
    https://en.wikipedia.org/wiki/Chaos_game

    Instead of explicitly drawing geometry, this approach:
    1. picks a random starting point inside a triangle
    2. randomly selects a vertex
    3. moves exactly halfway to that vertex
    4. and plots a dot
    
    Over thousands of iterations, the fractal emerges.
    
    Args:
        ax (matplotlib.axes.Axes): The subplot axis to draw on.
    """

    vertices = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.5, np.sqrt(3)/2]
    ])

    num_points = 50000
    points = np.zeros((num_points, 2))
    current_point = vertices[0]

    for i in range(num_points):
        random_vertex_index = np.random.randint(0, 3)
        target_vertex = vertices[random_vertex_index]
        current_point = (current_point + target_vertex) / 2.0
        points[i] = current_point

    ax.scatter(points[:, 0], points[:, 1], s=0.1, color='green')
    ax.axis('equal')
    ax.axis('off')
    ax.set_title(f'Sierpinski Triangle (Chaos Game)')


## Sierpinski Carpet
def sierpinski_carpet_plot(ax: Axes) -> None:
    """
    This plot uses NumPy matrix manipulation.

    Generates a 2D array representing a square grid.
    
    It recursively divides the grid into 3x3 blocks and "removes" (sets to zero) the center block of each section.
    
    Uses plt.imshow to render the matrix.

    Args:
        ax (matplotlib.axes.Axes): The subplot axis to draw on.
    """

    def get_carpet(depth):
        size = 3**depth
        carpet = np.ones((size, size))
        for i in range(depth):
            step = 3**i
            for x in range(step, size, 3 * step):
                for y in range(step, size, 3 * step):
                    carpet[x:x+step, y:y+step] = 0
        return carpet

    depth = 4 
    carpet = get_carpet(depth)

    ax.imshow(carpet, cmap='binary')
    ax.axis('off')
    ax.set_title(f'Sierpinski Carpet (Depth {depth})')


## Cantor Set
def cantor_set(ax: Axes) -> None:
    """
    Draws sequential generations of the fractal on descending vertical levels. 
    It starts with a single line segment and recursively removes the middle 
    third of every segment to form the next generation.
    
    Args:
        ax (matplotlib.axes.Axes): The subplot axis to draw on.
    """

    def cantor_set_recursion(x, y, length, depth):
        if depth == 0:
            ax.plot([x, x + length], [y, y], color='black', linewidth=4)
            return

        new_length = length / 3.0
        cantor_set_recursion(x, y, new_length, depth - 1)
        cantor_set_recursion(x + 2 * new_length, y, new_length, depth - 1)

    max_depth = 6
    for i in range(max_depth + 1):
        cantor_set_recursion(0, max_depth - i, 1, i)

    ax.axis('off') 
    ax.set_title(f'Cantor Set (Generations 0 to {max_depth})')


if __name__ == "__main__":
    print("starting")


    # Create a 2x2 grid of subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))

    # Pass the corresponding axis to each function
    koch_snowflake(axs[0, 0])
    sierpinski_triangle(axs[0, 1])
    sierpinski_carpet_plot(axs[1, 0])
    cantor_set(axs[1, 1])

    # Adjust layout and display
    plt.tight_layout()
    plt.show()



## Fractal Exploration ##
# How fractals are formed
# The math behind fractals
# How NumPy can be used to graph out and show different fractal patterns


# Different types of fractal patterns:
# - Mandelbrot Set -- very complicated
# - Koch Snowflake
# - Sierpinski Triangle
# - Sierpinski Carpet & Menger Sponge
# - Cantor Set  -- skip this one?

