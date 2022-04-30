import pygame
from Engine.Objects import Triangle_Group


class Renderer:
    def __init__(self, display_surface: pygame.Surface) -> None:
        self.display_surface = display_surface

    def draw_triangles(self, triangles: Triangle_Group):
        # draw triangles
        # lighting
        # sort triangles
        pass
