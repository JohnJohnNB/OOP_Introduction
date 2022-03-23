import turtle
import math

#1. definir dados iniciais
#2. desenhar o corpo da casa
#3. desenhar a porta
#4. desenhar a janela
#5. desenhar o telhado

t = turtle.Turtle()
t.speed(0)
x = 100

def corpodacasa(tart, dist):
    for _ in range(2):
        tart.forward(2*dist)
        tart.left(90)
        tart.forward(dist)
        t.left(90)

def porta(tart, dist):
    tart.forward(dist/3)
    tart.left(90)
    
    tart.forward(2*dist/3)
    tart.right(90)
    tart.forward(dist/3)
    tart.right(90)
    tart.forward(2*dist/3)
    
def janela(tart, dist):
    tart.up()
    tart.left(90)
    tart.forward(dist/2)
    tart.left(90)
    tart.fd(dist/3)
    tart.down()
    
    for _ in range(4):
        tart.fd(dist/3)
        tart.right(90)
        
def telhado(tart, dist):
    tart.up()
    tart.fd(2*dist/3)
    tart.right(90)
    tart.down()
    tart.fd(dist/2 + dist/3 + dist/6)
    tart.left(135)
    tart.fd(7/6*dist * math.sqrt(2))
    tart.left(90)
    tart.fd(7/6*dist * math.sqrt(2))
    tart.left(135)
    tart.fd(dist/6)
    
    
    
corpodacasa(t, x)
porta(t, x)
janela(t, x)
telhado(t, x)
