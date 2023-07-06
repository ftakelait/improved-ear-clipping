# Improved Ear Clipping for Faster and Robust Polygon Triangulation

This repository contains Python code to test the performance of an improved Ear Clipping algorithm for polygon triangulation. The improvement involves pre-sorting the vertices by their x-coordinate and using a tolerance value for degenerate cases.

## Contents

- `src/generate_polygon.py`: Code to generate a random polygon.
- `src/ear_clipping_basic.py`: Basic Ear Clipping algorithm implementation.
- `src/ear_clipping_improved.py`: Improved Ear Clipping algorithm implementation.
- `src/main.py`: Main script to measure the runtime of the two algorithms on a set of randomly generated polygons.

## Running the Code

To run the code, navigate to the `src` directory and run the `main.py` script:

```bash
cd src
python main.py
