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

# --- Making a mesh --- #

# Mesh will consist of a numpy array that holds all points
# Each point in array will be a Vector3

# --- To draw a mesh --- #

# points will be calcluated one by one
# points will be mapped into triangles
# coloring and texturing will be done for the triangle
# normal will be calculated for the triangle

""" Camera """

# Camera given own class for access
# Add functions for later expansion with movement


class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y}, z = {self.z})"

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"

    # __array__ is used by numpy when operations are done with a numpy array
    def __array__(self):
        return np.array([self.x, self.y, self.z], float)


class Mesh:
    pass


class Camera:
    pass


class Renderer:
    pass


def main():
    v = Vector3(1, 2, 3)
    print(v)


if __name__ == "__main__":
    main()
