# Python-Projects
This contains various projects on Python which i made when i was learning it.

# I've made a Figure using diiferent commands.

import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("yellow")
     
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(500)
    
    for i in range (1, 102):
        brad.right(1)
        brad.forward(120)
        brad.right(50)
        brad.forward(90)
        brad.right(120)
        brad.fd(90)
        brad.right(50)
        brad.forward(120)

    brad.right(90)    
    brad.fd(350)    
        
    window.exitonclick()

draw_triangle()    
