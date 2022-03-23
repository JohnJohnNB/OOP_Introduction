import turtle

t = turtle.Turtle()
t.speed(10)
t.left(90)
#####################################
def olho(tort):
    for i in range(100, 25, -25):
        tort.color('blue')
        tort.circle(i)
    
    tort.fillcolor('black')
    tort.begin_fill()
    tort.color('black')
    tort.circle(25)
    tort.end_fill()
#####################################
def nariz(tort):
    for _ in range(90):
    
        tort.fd(55)
        tort.left(180)
        tort.fd(55)
        tort.left(180)
        tort.left(4)
#####################################
def boca(tort):
    tort.width(8)
    tort.color('red')
    tort.circle(130, 45)
    tort.left(180)
    tort.circle(-130, 45)
    tort.circle(-130, 45)
#####################################
    
olho(t) ######### OLHO
t.up()
t.right(90)
t.fd(2)
t.right(90)
t.down()
olho(t)

t.up()
t.fd(160)
t.down()
t.color('magenta')

t.speed(0) ###### NARIZ
nariz(t)
t.color('black')
t.speed(10)


t.up()
t.fd(120)
t.left(90)
t.down()

boca(t) ###### BOCA

turtle.done()
 
    