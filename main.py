from turtle import *
import random
screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"




turtle1 = Turtle()
turtle1.shape("triangle")
turtle1.color("green")




def playing_area():
    Turtle.begin_fill()
    for i in range(sides):
        turtle.forward(50)
        turtle.left(360/ sides)
    turtle.end_fill()




def move_with_heading(t, turtles):
    direction = input("enter up,left,down,or right")
    if input == "up":
        turtle1.up(50)
    elif input == "left":
        turtle1.left(50)
    elif input == "down":
        turtle1.down(50)
    elif input == "right":
        turtle1.right(50)





def move_with_deltas(t, dx, dy):
    pass









screen.exitonclick()
playing_area()
move_with_heading(t, turtles)