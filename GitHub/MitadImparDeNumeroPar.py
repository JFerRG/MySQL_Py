def numDoble(num):
    nuevonum = num
    count = 0
    while True:
        if nuevonum % 2 == 0:
            nuevonum /= 2
            count +=1
        elif num % 2 == 1 or count > 1:
            print('{} no tiene miad impar'.format(num))
            break
        else:
            print('{0} es el doble de {1}, que es impar.'.format(num,nuevonum))
            break

    
while True:
    try:
        num = int(input('Ingresa un número: \n'))
        if num != 0:
            numDoble(num)
            break
    except Exception as e:
        print('Error al capturar el número, inténtalo nuevamente.')
        print(str(e))


