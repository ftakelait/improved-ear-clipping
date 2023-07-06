from shapely.geometry import Polygon

def ear_clipping_basic(polygon):
    """
    Basic Ear Clipping algorithm (no optimizations)
    """
    vertices = list(polygon.exterior.coords)[:-1]  # Ignore the last point because it's a repetition of the first
    triangles = []

    while len(vertices) > 3:
        for i in range(len(vertices)):
            a, b, c = vertices[i - 1], vertices[i], vertices[(i + 1) % len(vertices)]
            triangle = Polygon([a, b, c])
            
            if triangle.is_valid and triangle.area > 0 and triangle.contains(polygon):  # Valid "ear"
                triangles.append(triangle)
                vertices.pop(i)
                break
        else:
            raise Exception("No valid 'ear' found")
    
    if len(vertices) == 3:
        triangles.append(Polygon(vertices))
    
    return triangles
