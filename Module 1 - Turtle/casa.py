import turtle
import math


tortuga = turtle.Turtle()
x = 100

#RETANGULO
tortuga.fillcolor('blue')
tortuga.begin_fill()
for _ in range(2):
    tortuga.forward(2*x)
    tortuga.left(90)
    tortuga.forward(x)
    tortuga.left(90)
tortuga.end_fill()

#PORTA
tortuga.fillcolor('purple')
tortuga.begin_fill()
tortuga.forward(x/3)
tortuga.left(90)
tortuga.forward(2*x/3)
tortuga.right(90)
tortuga.forward(x/3)
tortuga.right(90)
tortuga.forward(2*x/3)
tortuga.end_fill()

tortuga.up()
tortuga.left(90)
tortuga.forward(x/4)
tortuga.left(90)
tortuga.forward(x/3)
tortuga.down()

#JANELA
tortuga.fillcolor('green')
tortuga.begin_fill()
for _ in range(4):
    tortuga.forward(x/3)
    tortuga.right(90)
tortuga.end_fill()

#JANELA2
tortuga.up()
tortuga.right(90)
tortuga.forward(x/3 + x/6)
tortuga.down()

tortuga.fillcolor('green')
tortuga.begin_fill()
for _ in range(4):
    tortuga.forward(x/3)
    tortuga.left(90)
tortuga.end_fill()

#TELHADO
tortuga.up()
tortuga.left(90)
tortuga.forward(2*x/3)
tortuga.right(90)
tortuga.down()

tortuga.fillcolor('red')
tortuga.begin_fill()
tortuga.forward(x/3 + x/3)
tortuga.left(135)
tortuga.forward((x + x/12) * math.sqrt(2))
tortuga.left(90)
tortuga.forward((x + x/12) * math.sqrt(2))
tortuga.left(135)
tortuga.forward(x/12 + x)
tortuga.end_fill()

#END
turtle.done()



