import numpy as np
from Engine.Vector import Vector3D


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
            return verticies, np.array(faces)

    except IOError:
        print(f"{file_name} could not be found")
        return np.array([]), np.array([])
