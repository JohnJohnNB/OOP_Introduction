import turtle

t = turtle.Turtle()
t.speed(10)
t.up()
t.goto(-300, 0)
t.down()


for raio in range(20, 68, 6):
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(raio)
    t.up()
    t.forward(2*raio + 6)
    t.down()
    t.end_fill()

turtle.done()
