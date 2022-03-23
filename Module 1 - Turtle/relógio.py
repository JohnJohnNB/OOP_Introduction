import turtle



t = turtle.Turtle()
t.speed(10)

t.width(2)
t.circle(100)
t.up()
t.left(90)
t.fd(10)
t.right(90)
t.down()

for x in range(12):
    t.dot(5)
    t.up()
    t.circle(90, extent=30)
    t.down()
    
t.up()
t.left(90)
t.fd(90)
t.left(60)
t.down()
t.width(4)
t.fd(50)

t.up()
t.right(180)
t.fd(50)
t.left(126)
t.down()

t.width(3/2)
t.color("red")
t.fd(88)

t.up()
t.right(180)
t.fd(88)
t.left(90)
t.down()

t.width(3)
t.color("black")
t.fd(82)

turtle.done()

    