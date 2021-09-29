import turtle

turtle.shape("turtle")

def w():
    turtle.forward(50)

def s():
    turtle.back(50)

def a():
    turtle.left(10)

def d():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

my_screen = turtle.Screen()

turtle.onkey(w, "w")
turtle.onkey(s, "s")
turtle.onkey(a, "a")
turtle.onkey(d, "d")
turtle.onkey(clear, "space")
turtle.listen()
my_screen.exitonclick()