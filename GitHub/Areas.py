import math

class Areas():
    def circulo(self,radio):
        return (math.pi * (radio**2))
    
    def triangulo1(self,h,b):
        return ((h*b)/2)

    def triangulo2(self,a,b,angulo):
        self.angulo = ((angulo*math.pi)/180)
        return ((1/2)*(a*b)*math.sin(self.angulo))

class PerimetrosReg():
    def Cuadrilatero(self,a,b):
        return((a*2)+(b*2))
    def Trilangulo(self,a,b,c):
        return(a+b+c)
    def Circulo(self,diametro):
        return (math.pi * diametro)