def validacion():
    while True:
        try:
            num = int(input('Ingresa el valor: '))
            if num > 0:
                return num
                break
            else:
                print('El número ha de ser mayor que cero')
        except Exception as e:
            print('Error al obtener el número\n' + str(e))
def dobles (a,b):
    if b == (a**2):
        print('{} es el cuadrado exacto de {}'.format(b,a))
    elif b < (a**2):
        print('{} es menor que el cuadrado de {}'.format(b,a))
    elif b > (a**2):
        print('{} es mayor que el cuadrado de {}'.format(b,a))

dobles(validacion(),validacion())

