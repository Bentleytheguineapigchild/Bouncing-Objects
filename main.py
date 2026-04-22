from turtle import *
import random
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def create_turtle():
    yertle = Turtle()
    yertle.color(generate_color())
    yertle.speed(0)
    yertle.shape("circle")
    yertle.setheading(random.randint(-2,2))
    return yertle










def move_heading(t, turtles):
    t.forward(5)
    if t.xcor() > 240 or t.xcor()< -240:
        t.setheading(180 - t.heading())
        turtles.append(create_turtle())
    if t.ycor() > 240 or t.ycor() < -240:
        t.setheading(-t.heading())
        turtles.append(create_turtle())
    return turtles
   








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


playing_area()
def create_player():
    global player
    player = Turtle()
    player.speed(0)
    player.color("black")
    player.shape("turtle")


def up():
    global player
    player.setheading(90)
    player.sety(player.ycor()+ 10)




def down():
    global player
    player.setheading(-90)
    player.sety(player.ycor() - 10)




def right():
    global player
    player.setheading(0)
    player.setx(player.xcor()+ 10)




def left():
    global player
    player.setheading(-90)
    player.setx(player.xcor()- 10)










player = None






screen = Screen()
screen.bgcolor("purple")
screen.setup(520,520)
screen.listen()
# key binding connects key presses and mouse clicks with function calls
screen.onkey(create_player, "space")
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(right, "d")
screen.onkeypress(left, "a")










yertle = Turtle()
yertle.color("red")
yertle.speed(0)
yertle.shape("turtle")


turtles = [yertle]


alive = True
while alive:
    for object in turtles:
        turtles = move_heading(object, turtles)
        # determines if the player and the object have touched
        if player != None and player.distance(object) < 20:
            object.hideturtle()
            turtles.remove(object)










turtles = [yertle]




screen.exitonclick()