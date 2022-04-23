import pygame
import numpy as np

""" Engine """

# small engine used to learn
# easy to play around with
# some more advanced features
# purely a learning project with python


""" Readability """

# --- Removing indicies --- #

# Vector3 class wil be made to use point with x, y , z
# https://numpy.org/doc/stable/user/basics.subclassing.html


""" Ease of Use """

# --- Renderer --- #

# Functions built to allow for easy use
# Take in meshes
# Draw them and / or texture them with one command
# simplify the process

# --- Meshes --- #

# Implement mesh generation
# Implement importing meshes
# Implement texturing meshes
# Give pre-made meshes


""" Meshes """

# --- Meshes will be made out of a set of points --- #

# meshes contain array of points
# meshes contain array of indicies to create triangles
# meshes contain an array of uv's to map textures
# meshes will have points calculated because python = slow

# --- To draw a mesh --- #

# points will be calcluated one by one
# points will be mapped into triangles
# coloring and texturing will be done for the triangle
# normal will be calculated for the triangle

""" Camera """

# Camera given own class for access
# Add functions for later expansion with movement


class Camera:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.pos = np.array([x, y, z], float)
        self.rotation = np.zeros(3, dtype=float)
        self.normal = np.zeros(3, dtype=float)


class Renderer:
    def __init__(self) -> None:
        pass


def main():
    a = np.array([1, 2, 3], float)
    print(a.data)


if __name__ == "__main__":
    main()
