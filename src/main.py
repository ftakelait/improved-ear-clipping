import time
from generate_polygon import generate_random_polygon
from ear_clipping_basic import ear_clipping_basic
from ear_clipping_improved import ear_clipping_improved

# Number of polygons to generate for each size
num_polygons = 100

# Create a list of random polygons for each vertex count
polygons = [generate_random_polygon(vertex_count) for _ in range(num_polygons) for vertex_count in range(3, 101)]

print("Running basic Ear Clipping...")

start = time.time()
for polygon in polygons:
    triangles = ear_clipping_basic(polygon)
end = time.time()

print(f"Basic Ear Clipping took {end - start} seconds for {num_polygons} polygons.")

print("Running improved Ear Clipping...")

start = time.time()
for polygon in polygons:
    triangles = ear_clipping_improved(polygon)
end = time.time()

print(f"Improved Ear Clipping took {end - start} seconds for {num_polygons} polygons.")
