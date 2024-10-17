# Python-Hirst-Art-Simulation
This repo uses the Python turtle module to create a Hirst-inspired dot painting. The program generates a grid of colored dots, each picked randomly from a predefined list of RGB color values, using Turtle graphics.

# Project Overview
The code simulates a simple painting composed of 100 dots, each filled with a random color from a list of 30 different colors. The turtle graphics library is used to:
 - Create and position the turtle.
 - Draw the dots in rows, resetting the turtle position after each row to form a grid.

# Features
- Random Colors: The dot colors are chosen randomly from a list of predefined RGB colors.
- Grid Layout: The dots are arranged in a 10x10 grid.
- Turtle Graphics: The turtle module is used to simulate the drawing process.

# Requirements
- Python: The code is written in Python and uses the built-in turtle module.
- Turtle: The turtle module is part of the Python standard library and does not require external installation.

# Code Explanation
1. Color Extraction:
  - A list of colors, color_list, is predefined in the script. These are RGB tuples representing various colors.
  - The code includes commented-out lines using colorgram to extract colors from an image. You can use colorgram to customize your own color list.

2. Turtle Setup:

  - The turtle is initialized with the coco object.
  - It is set to "fastest" speed for quicker drawing.
  - penup() ensures the turtle moves without drawing unnecessary lines.

3. Dot Drawing:

  - The turtle moves across the screen in a grid pattern.
  - Every iteration places a colored dot, then moves the turtle forward.
  - After every 10 dots (end of each row), the turtle moves to the start of the next row.

4. Screen Exit:

  - The script waits for the user to click on the screen to exit (exitonclick()).

# Customization
- Change Colors: Update the color_list to change the palette used in the painting.
- Change Grid Size: Modify the num_of_dots and the loop to create a larger or smaller grid.
- Dot Size: You can adjust the dot size by changing the coco.dot(20, ...) to a different value.

Enjoy creating digital art using Python's turtle graphics!
