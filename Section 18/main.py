# # from turtle import Turtle, Screen
# # from turtle import * # import la tot
# # import turtle as t
#
# # tim = Turtle()
# # tim.shape("turtle")
# # tim.color("green yellow")
# # for _ in range(4):
# #     tim.right(90)
# #     tim.forward(100)
#
# import turtle as t
# import random
# tim = t.Turtle()
#
# ########### Challenge subreddits - Draw a Dashed Line ########
#
# # for _ in range(15):
# #     tim.fd(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
# # colours = ["CornflowerBlue", "DarkOrchid"]
# # for i in range(3,11):
# #     s = 360 / i
# #     while i != 0:
# #         tim.color(random.choice(colours))
# #         tim.right(s)
# #         tim.forward(100)
# #         i -=1
#
# ########### Challenge 4 - Random Walk ########
#
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = t.Screen()
# screen.exitonclick()

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
########### Challenge 5 - Spirograph ########
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()