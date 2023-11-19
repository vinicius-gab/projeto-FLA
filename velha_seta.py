from turtle import Turtle, Screen, onkey, listen, onkeypress
turtle = Turtle()
tela = Screen()
tela.bgcolor("black")
def montar_jogo():
    for _ in range(4):
        turtle.color("white")
        turtle.shape("turtle")
        turtle.forward(100)
        turtle.back(200)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.back(200)
        turtle.forward(100)
        turtle.left(90)

def circulo():
    turtle.color("cyan")
    turtle.shape("circle")
    turtle.circle(25)

def vx():
    turtle.color("red")
    turtle.shape("arrow")
    turtle.left(45)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.left(45)

def up():
    y_atual = turtle.ycor()
    turtle.penup()
    novo_y = y_atual + 10
    turtle.sety(novo_y)
    turtle.pendown()

def down():
    y_atual = turtle.ycor()
    turtle.penup()
    novo_y = y_atual - 10
    turtle.sety(novo_y)
    turtle.pendown()

def right():
    x_atual = turtle.xcor()
    turtle.penup()
    novo_x = x_atual + 10
    turtle.setx(novo_x)
    turtle.pendown()

def left():
    x_atual = turtle.xcor()
    turtle.penup()
    novo_x = x_atual - 10
    turtle.setx(novo_x)
    turtle.pendown()

def diagonal():
    turtle.left(45)
    turtle.forward(300)
    
montar_jogo()
onkeypress(up, "Up")
onkeypress(down, "Down")
onkeypress(right, "Right")
onkeypress(left, "Left")
onkey(vx, "x")
onkey(circulo, "o")
listen()
tela.mainloop()