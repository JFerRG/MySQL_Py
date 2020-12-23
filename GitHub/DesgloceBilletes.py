def desgloce(num):
    values = [500,200,100,50,20,10,5,2,1]
    cant = []
    for i in range(len(values)):
        valor = int(num/values[i])
        if valor != 0:
            cant.append(valor)
            num = num%values[i]
        else:
            cant.append(valor)
    
    for i in range(len(cant)):
        if cant[i] != 0:
            if values[i] > 10:
                print("Necesitamos {} billete/s de {}".format(cant[i],values[i]))
            else:
                print("Necesitamos {} moneda/s de {}".format(cant[i],values[i]))
        else:
            continue

try:
    num = int(input("Ingrese la cantidad a evaluar:\n"))
    desgloce(num)
except Exception as e:
    print("Error al obtener el número:\n" + str(e))

