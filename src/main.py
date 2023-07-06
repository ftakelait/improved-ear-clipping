import time
from generate_polygon import generate_random_polygon
from ear_clipping_basic import ear_clipping_basic
from ear_clipping_improved import ear_clipping_improved

def main():
    # Generate dataset
    num_polygons = 100
    polygons = [generate_random_polygon(vertex_count) for vertex_count in range(3, 101) for _ in range(num_polygons)]
    
    times_basic = []
    times_improved = []

    for polygon in polygons:
        try:
            # print("Running basic Ear Clipping...")
            start = time.time()
            triangles = ear_clipping_basic(polygon)
            for ear in ear_clipping_basic(polygon):
                print(ear)
            end = time.time()
            times_basic.append(end - start)
            # print("Basic Ear Clipping done.")

            # print("Running improved Ear Clipping...")
            start = time.time()
            triangles = ear_clipping_improved(polygon)
            end = time.time()
            times_improved.append(end - start)
            # print("Improved Ear Clipping done.")
        except Exception as e:
            # Skip the current polygon if no ear is found in the basic algorithm
            if str(e) == "No valid 'ear' found":
                continue
            print(f"Exception for polygon: {polygon}\n{e}")

    print(f"Average time for Basic Ear Clipping: {sum(times_basic) / len(times_basic)} seconds")
    print(f"Average time for Improved Ear Clipping: {sum(times_improved) / len(times_improved)} seconds")

if __name__ == "__main__":
    main()
