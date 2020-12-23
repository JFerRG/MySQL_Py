import turtle

turtle.delay(10)
turtle.pen(pensize=2)

turtle.pen(pencolor='green')
turtle.circle(20)
turtle.pen(pencolor='yellow')
turtle.right(90)
turtle.forward(10)
turtle.left(90)

turtle.pen(pencolor='blue')
turtle.circle(30)

turtle.pen(pencolor='yellow')
turtle.right(90)
turtle.forward(20)
turtle.backward(100)
turtle.forward(50)

turtle.pen(pencolor='purple',fillcolor='red')
turtle.right(90)
turtle.forward(50)
turtle.backward(100)
turtle.forward(50)

turtle.pen(pencolor='red',fillcolor='red')
turtle.shape('circle')

turtle.exitonclick()

