from turtle import *
import random
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def move_heading(t):
    t.forward(5)
    if t.xcor() > 240:
        t.setheading(180)
    if t.xcor() < -240:
        t.setheading(0)
   

def playing_area():
    pen = Turtle()
    pen.color("yellow")
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(240,240)
    pen.end_fill()


screen = Screen()
screen.bgcolor("purple")
screen.setup(520,520)

playing_area()




yertle = Turtle() 
yertle.color("red")
yertle.speed(0)
yertle.shape("turtle")
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)

def move_xy(turtle, deltax, deltay):
    newy = turtle.ycor()+ deltay
    if newy > 240 or newy < -240:
        newy = turtle.ycor()
        deltay *= -1


    newx = turtle.xcor()+ deltax
    if newx > 240 or newx < -240:
        newx = turtle.xcor()
        deltax *= -1
    turtle.goto(newx, newy)

    return deltax, deltay

alive = True
while alive:
    deltax, delay = move_xy(yertle,deltax,deltay)

    


screen.exitonclick()