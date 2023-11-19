from turtle import Turtle, Screen, onscreenclick
from random import randint
turtle = Turtle()
tela = Screen()
jogada = 0

def jump(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def montar_jogo():
    for _ in range(4):
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

def circulo(a):
    turtle.circle(a)

def vx():
    turtle.left(45)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.left(45)
def desenho(x, y):
    global jogada
    jump(x, y)
    jogada += 1
    if (jogada % 2 == 1):
        vx()
    else:
        circulo(25)

montar_jogo()
onscreenclick(desenho)
tela.mainloop()