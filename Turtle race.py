from turtle import *
from random import *

bgcolor("sky blue")
title("Turtle Race")
speed(0)
penup()
goto(-140, 140)

for step in range(16):
    write(step, align="center")         # align= za centriranje brojeva iznad linije
    right(90)
    forward(10)

    # isprekidane linije:
    for dash in range(10):
        pendown()
        forward(7)
        penup()
        forward(8)

    penup()
    backward(160)
    left(90)
    forward(20)
hideturtle()

# definisanje kornjaca:

#----------------------------------------------------------

a = Turtle()
a.color("red")
a.shape("turtle")

a.penup()
a.goto(-160, 100)
a.pendown()

#----------------------------------------------------------

b = Turtle()
b.color("blue")
b.shape("turtle")

b.penup()
b.goto(-160, 70)
b.pendown()

#----------------------------------------------------------

c = Turtle()
c.color("orange")
c.shape("turtle")

c.penup()
c.goto(-160, 40)
c.pendown()

#----------------------------------------------------------

d = Turtle()
d.color("green")
d.shape("turtle")

d.penup()
d.goto(-160, 10)
d.pendown()

# za okretanje kornjace oko sebe prije trke:

for twirl in range(1):
    a.right(36*10)
    b.left(72*5)
    c.right(36*10)
    d.left(72*5)

# trka/race:

for turn in range(100):
    a.forward(randint(1, 5))
    b.forward(randint(1, 5))
    c.forward(randint(1, 5))
    d.forward(randint(1, 5))


done()