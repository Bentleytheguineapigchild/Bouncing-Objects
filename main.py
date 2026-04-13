from turtle import *
import random


def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    screen.border("lime")


def move_with_heading(t, turtles):
    pass



def move_with_deltas(t, dx, dy):
    pass





screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)



screen.exitonclick()
playing_area()