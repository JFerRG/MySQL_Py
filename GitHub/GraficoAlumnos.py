import turtle
import random

class Grafica:
    def __init__(self,datos):
        turtle.hideturtle()
        self.datos = datos
        self.inicio()
        may = max(self.datos)
        for i in self.datos:
            disy = (i*500)/may
            #disy = i
            self.colores()
            turtle.begin_fill()
            turtle.forward(disy)
            turtle.right(90)
            turtle.forward(30)
            turtle.right(90)
            turtle.forward(disy)
            turtle.left(90)
            turtle.end_fill()
            turtle.forward(10)
            turtle.left(90)

        turtle.exitonclick()

    def inicio(self):
        turtle.penup()
        turtle.backward(400)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(350)
        turtle.backward(700)
        turtle.right(90)
        turtle.forward(800)
        turtle.backward(790)
        turtle.left(90)

    def colores(self):
        turtle.colormode(255)
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)
        turtle.fillcolor((r,g,b))
grafico = Grafica([20,30,40,50,60,70,80,90,100,30,40,20,10])