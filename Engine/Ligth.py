from Engine.Vector import Vector3D

class Light:
    def __init__(self, position: list, rotation: list) -> None:
        self.pos = Vector3D(position[0], position[1], position[2])
        self.normal = self.pos.normalize()