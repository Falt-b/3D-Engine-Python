import numpy as np
from Engine.Vector import Vector3D


class Triangle_Group:
    def __init__(self) -> None:
        self.tris = np.array([].object)

    def add_tri(self, tris: np.ndarray):
        self.tris = np.append(self.tris, tris)


class Mesh:
    def __init__(self, points: np.array, triangles: np.array) -> None:
        self.points = points
        self.triangles = triangles


class Object3D:
    def __init__(self, position: list, rotation: list, mesh: Mesh) -> None:
        self.pos = Vector3D(position[0], position[1], position[2])
        self.rot = Vector3D(rotation[0], rotation[1], rotation[3])
        self.mesh = mesh

    def rotate_x(self, angle: float):
        pass

    def rotate_y(self, angle: float):
        pass

    def rotate_z(self, angle: float):
        pass
