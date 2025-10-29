with open('day7\\input.txt','r') as entrada:
    datos = entrada.readlines()

'''datos = [
'190: 10 19',
'3267: 81 40 27',
'83: 17 5',
'156: 15 6',
'7290: 6 8 6 15',
'161011: 16 10 13',
'192: 17 8 14',
'21037: 9 7 18 13',
'292: 11 6 16 20'
]'''

# Esta función devuelve ternarios, ya que la parte anterior la hice con binarios
def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

# Voy a probar a hacerlo en binario ya que me permitirá recorrer todas las posibles operaciones

total = 0
for linea in datos:
    # Estas tres lineas me separan los datos en un int con el resultado y una lista con los números que probar
    resultado = linea.split(':')[0]
    numeros = linea.split()
    numeros.remove(resultado + ':')
    
    # Para cada linea reinicio los valores de cuentas y operadores

    operadores = 0
    for j in range(3 ** len(numeros)):
        flag = False
        op_ter = 100*'0'+ternary(operadores)
        cuentas = int(numeros[0])
        for i in range(len(numeros) - 1):
            if op_ter[-(i+1)] == '0':
                cuentas += int(numeros[i+1])
            elif op_ter[-(i+1)] == '1':
                cuentas *= int(numeros[i+1])
            elif op_ter[-(i+1)] == '2':
                aux = str(cuentas)
                cuentas = int(aux + str(numeros[i+1]))
            if cuentas == int(resultado):
                total += int(resultado)
                flag = True
                break
        operadores += 1
        if flag == True:
            break

print(total)