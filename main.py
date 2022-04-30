import pygame
import numpy as np

WIDTH = 600
HEIGHT = 600
FRAME_CAP = 60
BG_COLOR = (20, 20, 20)
ASPECT_RATIO = WIDTH / HEIGHT


class Vector3D(pygame.Vector3):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        self.w = 1

    def __repr__(self) -> str:
        return f"\n[{self.x}, {self.y}, {self.z}, {self.w}]"

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}, {self.w}]"

    def __array__(self, dtype):
        return np.array([self.x, self.y, self.z, self.w], dtype)

    def normalize(self):
        n = self.x**2 + self.y**2 + self.z**2
        return Vector3D(self.x / n, self.y / n, self.z / n)


class Triangle_Group:
    def __init__(self) -> None:
        self.tris = np.array([])

    def add_tri(self, tris: np.ndarray):
        self.tris = np.append(self.tris, tris)
        self.tris = np.reshape(self.tris, (-1, 5))


class Mesh:
    def __init__(self, points: np.ndarray, triangles: np.ndarray) -> None:
        self.points = points
        self.triangles = triangles

    def __str__(self) -> str:
        return f"Points:\n {self.points} \n\n Faces:\n {self.triangles}"


class Object3D(Mesh):
    def __init__(self, position: list, rotation: list, mesh: Mesh) -> None:
        super().__init__(mesh.points, mesh.triangles)
        self.position = Vector3D(position[0], position[1], position[2])
        self.rotation = Vector3D(rotation[0], rotation[1], rotation[3])

    def rotate_x(self, angle: float):
        s, c = np.sin(angle), np.cos(angle)
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], np.float16)

    def rotate_y(self, angle: float):
        s, c = np.sin(angle), np.cos(angle)
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]], np.float16)

    def rotate_z(self, angle: float):
        s, c = np.sin(angle), np.cos(angle)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], np.float16)

    def calculate_triangles(self):
        rotation_x = self.rotate_x(self.rotation.x)
        rotation_y = self.rotate_y(self.rotation.y)
        rotation_z = self.rotate_z(self.rotation.z)
        for triangle in self.triangles:
            tri = [
                self.points[triangle[0]],  # should be a Vector3D
                self.points[triangle[1]],
                self.points[triangle[2]],
            ]


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


class Light:
    def __init__(self, position: list, rotation: list) -> None:
        self.pos = Vector3D(position[0], position[1], position[2])
        self.normal = self.pos.normalize()


class Renderer:
    def __init__(
        self,
        display_surface: pygame.Surface,
        show_normals: bool = False,
        show_wire_frame: bool = False,
    ) -> None:
        self.display_surface = display_surface
        self.show_normals = show_normals
        self.show_wire_frame = show_wire_frame

    """ Rendering """

    # Handle triangles from a group
    # draw other items if requested
    # only draw triangles
    # points are pre calculated
    # possilbly calculate triangles lighting


def load_object(file_name: str):
    try:
        with open(file_name) as f:
            verticies = []
            faces = []
            for line in f:
                if line[0] == "v":
                    l = str(line[1:]).split()
                    verticies.append(Vector3D(float(l[0]), float(l[1]), float(l[2])))

                if line[0] == "f":
                    l = str(line[1:]).split()
                    faces.append([int(l[0]) - 1, int(l[1]) - 1, int(l[2]) - 1])
            return Mesh(verticies, np.array(faces, np.int8))

    except IOError:
        print(f"{file_name} could not be found")
        return Mesh([], np.array([], np.int8))


def draw_triangle(surface: pygame.Surface, triangle: np.ndarray, fill: int = 0):
    # fix later to take in triangle color to draw with
    # triangle format
    # [v1, v2. v3, normal, color]
    pygame.draw.polygon(
        surface,
        (255, 255, 255),
        (
            (triangle[0].x, triangle[0].y),
            (triangle[1].x, triangle[1].y),
            (triangle[2].x, triangle[2].y),
        ),
        fill,
    )


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
