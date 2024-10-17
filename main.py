# import colorgram
import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 48)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle_module.colormode(255)
coco = turtle_module.Turtle()
coco.speed("fastest")
coco.penup()
coco.hideturtle()
color_list = [(253, 248, 251), (208, 77, 137), (245, 145, 71), (236, 225, 87), (250, 47, 18), (79, 199, 238), (70, 205, 154), (92, 110, 201), (179, 56, 37), (243, 150, 202), (74, 91, 167), (55, 175, 42), (226, 128, 167), (35, 120, 58), (39, 76, 55), (7, 191, 212), (142, 188, 245), (96, 40, 55), (158, 37, 19), (22, 39, 96), (48, 66, 42), (251, 158, 2), (91, 50, 29), (103, 216, 245), (149, 69, 86), (31, 46, 104), (244, 171, 151), (145, 216, 184), (77, 35, 46), (66, 68, 42)]

coco.setheading(225)
coco.forward(300)
coco.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    coco.dot(20, random.choice(color_list))
    coco.forward(50)

    if dot_count % 10 == 0:
        coco.setheading(90)
        coco.forward(50)
        coco.setheading(180)
        coco.forward(500)
        coco.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()