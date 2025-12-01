# Tenemos que encontrar la forma de seleccionar los strings donde ponga exactamente mul(a,b) donde a y b son números de entre 1 y 3 cifras
# Con esto el problema estaría básicamente hecho, el resultado será sumar todos los a*b de este tipo
import re
with open('2024\\day3\\input.txt','r') as entrada: # Dos barras para indicar que es una barra y no espere una acción después, como si fuera \t o \n
    datos = entrada.read()

final = re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)',datos)

i = 0
flag = True
resultado = 0
for elemento in final:
    if elemento == 'do()':
        flag = True
        continue
    elif elemento == 'don\'t()':
        flag = False
    if flag == True:
        numeros = re.findall(r'[0-9]+',elemento)
        producto = int(numeros[0]) * int(numeros[1])
        i += 1
        resultado += producto
print(resultado)

