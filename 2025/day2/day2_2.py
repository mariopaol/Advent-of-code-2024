with open('2025\\day2\\input.txt','r') as entrada:
    datos = entrada.readlines()
datos_individuales = datos[0].split(',')

resultado = 0
for rango in datos_individuales:
    rango_min = int(rango.split('-')[0])
    rango_max = int(rango.split('-')[1])
    for i in range(rango_min , rango_max + 1):
        # Tengo que dividir el código en partes iguales. Como máximo en 2 partes del mismo tamaño. Para ello, debo comprobar si es divisible entre
        # todos los números hasta len(string) // 2
        for j in range(1, ( len(str(i)) // 2) + 1):
            lista = []
            if len(str(i)) % j != 0:
                continue
            for k in range(len(str(i)) // j):
                lista.append(str(i)[k * j : (k + 1) * j])
            if all(x == lista[0] for x in lista): # Si todos los elementos de la lista son iguales al primero
                resultado += i
                break
print(resultado)