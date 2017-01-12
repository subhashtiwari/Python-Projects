# Python-Projects
This contains various projects on Python which i made when i was learning it.
echo "# Python-Projects" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/subhashtiwari/Python-Projects.git
git push -u origin master

# THis code is for making different shapes.

import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(3)

    for i in range(0, 4):    
        brad.forward(170)
        brad.right(90)
    

    henry = turtle.Turtle()
    henry.shape("arrow")
    henry.color("green")
    henry.fillcolor("pink")
    henry.speed(3)
    henry.circle(90)

    tesla = turtle.Turtle()
    tesla.shape("turtle")
    tesla.color("blue")
    tesla.speed(3)
    tesla.backward(150)
    tesla.right(45)
    tesla.forward(212.13)
    tesla.left(135)
    tesla.forward(150)
    
    window.exitonclick()

draw_shapes()
