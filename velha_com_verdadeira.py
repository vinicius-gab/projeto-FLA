from turtle import Turtle, Screen, onscreenclick
turtle = Turtle()
tela = Screen()
jogada = True

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
    turtle.color("red")
    turtle.circle(a)

def vx():
    turtle.color("blue")
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
    if jogada:
        circulo()
    else:
        vx()
    jogada = not jogada

montar_jogo()
onscreenclick(desenho)
tela.mainloop()