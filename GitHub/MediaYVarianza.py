from math import sqrt
def llenado(lista):
    for i in range(5):
        while True:
            try:
                lista.append(float(input('Ingrese el numero {}\n'.format(i+1))))
                break
            except:
                print('Solo puede ingresar números enteros')   

valores = []
llenado(valores)
media = float(sum(valores)/len(valores))
print(media)

x = 0
for xi in valores:
    x += ((xi - media)**2)
var = float(x/5)
print(var)
des = sqrt(var)
print(des)

