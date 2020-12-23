def calcularIVA(precio):
    return (float(1.16*precio))

while True:
    try:
        valfin = calcularIVA(float(input('Ingrese el precio de un producto sin IVA:\n')))
        break
    except Exeption as e:
        print('Solo puede ingresar números;\n',e)

print(valfin)