import turtle

window = turtle.Screen()

turtle.delay(0)
turtle.shape(None)

def figuras(lados):
    i = 0
    for i in range(lados):
        turtle.forward(100)
        turtle.left(360/lados)
        i+= 1
def figuras2(lados):
    i = 0
    for i in range(lados):
        turtle.forward(100)
        turtle.right(abs((360/lados)-360))
        i+= 1

for i in range(5):
    figuras(4)
    turtle.left(22.5)

turtle.right(22.5)
turtle.forward(100)
turtle.left(180)

for i in range(5):
    figuras2(4)
    turtle.right(22.5)


turtle.exitonclick()