import turtle

t = turtle.Turtle()
t.speed(0)

t.up()
t.circle(80, extent = 45)
t.down()

for x in range(4):
    t.circle(80, extent = 90)
    t.left(90)
    t.circle(80, extent = 90)
    t.left(45)
    
t.up()
t.circle(80, extent = 90)
t.left(90)
t.circle(80, extent = 90)
t.left(45)
t.down()

for x in range(3):
    t.circle(80, extent = 90)
    t.left(90)
    t.circle(80, extent = 90)
    t.left(45)

t.right(135)
t.width(4)
t.fd(200)

t.up()
t.left(180)
t.fd(70)
t.right(90)
t.down()

t.fillcolor('black')
t.begin_fill()
t.left(15)
t.width(2)
t.fd(15)
t.left(165)
t.circle(-50, extent = 15)
t.end_fill()

t.width(1)
t.up()
t.left(105)
t.fd(7)
t.left(105)
t.fd(7)

t.down()
t.circle(60, extent = 50)
t.left(130)
t.circle(60, extent = 50)
t.up()
t.fd(50)

turtle.done()


