# Python-Projects
This contains various projects on Python which i made when i was learning it.

# In this code I Write My Initials.

import turtle

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.speed(100)
    brad.bk(80)
    brad.rt(90)
    brad.fd(60)
    brad.lt(90)
    brad.fd(80)
    brad.rt(90)
    brad.fd(60)
    brad.rt(90)
    brad.fd(80)

    brad.penup()
    brad.goto(100,0)

    brad.pendown()
    brad.fd(80)
    brad.bk(40)
    brad.lt(90)
    brad.fd(120)
   
    window.exitonclick()

draw_initials()    
