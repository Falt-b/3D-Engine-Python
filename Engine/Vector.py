import pygame
import numpy as np


class Vector3D(pygame.Vector3):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        self.w = 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y}, z = {self.z}, w = {self.w})"

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}, {self.w}]"

    def __array__(self):
        return np.array([self.x, self.y, self.z, self.w])
