with open('2024\\day7\\input.txt','r') as entrada:
    datos = entrada.readlines()


# Voy a probar a hacerlo en binario ya que me permitirá recorrer todas las posibles operaciones

total = 0
for linea in datos:
    # Estas tres lineas me separan los datos en un int con el resultado y una lista con los números que probar
    resultado = linea.split(':')[0]
    numeros = linea.split()
    numeros.remove(resultado + ':')
    
    # Para cada linea reinicio los valores de cuentas y operadores

    operadores = 0
    for j in range(2 ** len(numeros)):
        flag = False
        op_bin = f'{operadores:0500b}'
        cuentas = int(numeros[0])
        for i in range(len(numeros) - 1):
            if op_bin[-(i+1)] == '0':
                cuentas += int(numeros[i+1])
            elif op_bin[-(i+1)] == '1':
                cuentas *= int(numeros[i+1])
            if cuentas == int(resultado):
                total += int(resultado)
                flag = True
                break
        operadores += 1
        if flag == True:
            break

print(total)