# Python-Projects
This contains various projects on Python which i made when i was learning it.
echo "# Python-Projects" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/subhashtiwari/Python-Projects.git
git push -u origin master

# This Code is for making a Square & a Circle.
import turtle

def draw_circquare():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(10)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)

    henry = turtle.Turtle()
    henry.shape("arrow")
    henry.color("green")
    henry.circle(100)
    window.exitonclick()

draw_circquare()
