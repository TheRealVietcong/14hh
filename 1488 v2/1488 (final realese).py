import turtle as hh


hh.bgcolor("red")

hh.shape("turtle")
hh.color("white","white")
hh.begin_fill()
hh.pensize(5)

hh.penup()
hh.goto(0, -130)
hh.pendown()
hh.circle(130)
hh.end_fill()
hh.hideturtle()


b=[70,70,70,70]
a=70
for a in b:
    hh.penup()
    hh.goto(0,0)
    hh.pendown()
    hh.color("black")
    hh.pensize(25)
    hh.right(45)
    hh.forward(a)
    hh.right(90)
    hh.forward(a)
    hh.left(180)
    hh.forward(a)
    hh.left(90)
    hh.forward(a)
    hh.left(135)
hh.exitonclick()

