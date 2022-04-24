import pygame
import numpy as np

WIDTH = 600
HEIGHT = 600
FRAME_CAP = 60
BG_COLOR = (20, 20, 20)
ASPECT_RATIO = WIDTH / HEIGHT

""" Engine """

# small engine used to learn
# easy to play around with
# some more advanced features
# purely a learning project with python

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

# Add functions for later expansion with movement


""" Different array types """

# Using different array types for containers will help speed
# meshes could contain hundreds of points
# numpy arrays that hold Vector3's


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

    def normalize(self):
        n = self.x**2 + self.y**2 + self.z**2
        return Vector3(self.x / n, self.y / n, self.z / n)


class Camera:
    def __init__(
        self,
        position: list,
        rotation: list,
        fov: int,
        max_view_dist: float,
        min_view_dist: float,
    ) -> None:
        self.pos = Vector3(position[0], position[1], position[2])
        self.rot = Vector3(rotation[0], rotation[1], rotation[2])
        self.normal = self.pos.normalize()
        self.fov = fov
        self.max = max_view_dist
        self.min = min_view_dist


class Light:
    def __init__(self, position: list, rotation: list) -> None:
        self.pos = Vector3(position[0], position[1], position[2])

        # only for directional light implementation
        # self.rot = Vector3(rotation[0], rotation[1], rotation[3])

        self.normal = self.pos.normalize()

    # --- Multiple Lights --- #

    # for scenes with multiple lights
    # the normal of each light will be taken
    # the normals with then be averaged
    # or they will be weighted depending on the angle of the surface normal
    # if the light will even hit the surface


class Mesh:
    def __init__(self, points: np.array, triangles: np.array) -> None:
        self.points = points
        self.triangles = triangles


class Object3D:
    def __init__(self, position: list, rotation: list, mesh: Mesh) -> None:
        self.pos = Vector3(position[0], position[1], position[2])
        self.rot = Vector3(rotation[0], rotation[1], rotation[3])
        self.mesh = mesh

    # Object3D will take responsibility for everything with it's mesh


class Renderer:
    pass

    # --- Rendering --- #

    # how will triangles be passed into the renderer

    # add options for wire-frame view
    # add option for showing surface normals
    # normals will come from center of triangle


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("3D Engine in python")
    clock = pygame.time.Clock()
    t = 0
    dt = 0
    last_frame = 0
    running = True

    while running:
        clock.tick(FRAME_CAP)
        t = pygame.time.get_ticks()
        dt = (t - last_frame) / 1000
        last_frame = t
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(BG_COLOR)

        pygame.display.update()


if __name__ == "__main__":
    main()
