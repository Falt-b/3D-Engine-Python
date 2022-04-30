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
