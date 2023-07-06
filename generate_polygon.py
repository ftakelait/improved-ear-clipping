from shapely.geometry import Polygon
import random
import numpy as np

def generate_random_polygon(vertex_count):
    """
    Generate a random polygon with a specified number of vertices
    """
    angle_step = 2 * np.pi / vertex_count
    polygon_vertices = []
    for i in range(vertex_count):
        radius = 1.0 + 0.5 * random.random()
        angle = i * angle_step
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        polygon_vertices.append((x, y))
    random.shuffle(polygon_vertices)
    return Polygon(polygon_vertices)
