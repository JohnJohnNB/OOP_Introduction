import turtle
import math


t = turtle.Turtle()
t.speed(0)
npetalas = 7
def petala(tartaruga, lado, arco):
    tartaruga.circle(lado, arco)
    tartaruga.left(180-arco)
    tartaruga.circle(lado, arco)
    tartaruga.left(180-arco)

for _ in range(7):
    petala(t, 100, 80)
    t.right(360/npetalas)
