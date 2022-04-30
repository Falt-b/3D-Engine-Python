import numpy as np
from Engine.Vector import Vector3D


class Camera:
    def __init__(
        self,
        position: list,
        rotation: list,
        fov: int,
        max_view_dist: float,
        min_view_dist: float,
        screen_wdith: int,
        screen_height: int,
    ) -> None:
        self.pos = Vector3D(position[0], position[1], position[2])
        self.rot = Vector3D(rotation[0], rotation[1], rotation[2])
        self.aspect_ratio = screen_wdith / screen_height
        self.normal = self.pos.normalize()
        self.fov = np.deg2rad(fov)
        self.max = max_view_dist
        self.min = min_view_dist
        self.projection_matrix = np.array(
            [
                [self.aspect_ratio * self.fov, 0, 0, 0],
                [0, self.fov, 0, 0],
                [0, 0, self.max / (self.max - self.min), 1],
                [0, 0, (-self.max * self.min) / (self.max - self.min), 0],
            ],
            np.float16,
        )
