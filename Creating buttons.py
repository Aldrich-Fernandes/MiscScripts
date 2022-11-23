#Imports
import turtle

#Adding Icons
turtle.addshape(name="Ping Pong\Exit_Icon.gif", shape=None)

#Setting up a screen
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor('Black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Function for buttons
def Quit(x,y):
    if (x > -80 and x < -20) and (y < -310 and y > -340):
        wn.bye()

#Buttion for exit
ExitButton = turtle.Turtle()
ExitButton.penup()
ExitButton.speed(0)
ExitButton.shape("Ping Pong\Exit_Icon.gif")
ExitButton.pencolor("white")
ExitButton.setx(-50)
ExitButton.sety(-325)
ExitButton.shapesize(1.5, 3)
ExitButton.goto(-50, -325)

#Border
Border = turtle.Turtle()
Border.color("white")
Border.hideturtle()
Border.penup()
Border.goto(400,300)
Border.pendown()
Border.goto(400,-300)
Border.goto(-400,-300)
Border.goto(-400,300)
Border.goto(400,300)

#Main game loop
while True:
    #calling the function by click
    wn.onclick(Quit)
    wn.update()

    