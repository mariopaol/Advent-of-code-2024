# Tenemos que encontrar la forma de seleccionar los strings donde ponga exactamente mul(a,b) donde a y b son números de entre 1 y 3 cifras
# Con esto el problema estaría básicamente hecho, el resultado será sumar todos los a*b de este tipo
import re
with open('day3\\input.txt','r') as entrada: # Dos barras para indicar que es una barra y no espere una acción después, como si fuera \t o \n
    datos = entrada.read()

final = re.findall(r'mul\([0-9]+,[0-9]+\)',datos)
print(final)

# Supongamos que ya funciona usando final = re.findall(r'mul\([0-9]+,[0,9]+\)',datos), que no funciona y no se por qué. Ya se, el segundo, [0,9], debería ser [0-9]
# Para cada elemento tengo que encontrar el primer número que está entre '( y ',' y el segundo número que está entre ',' y ')'
i = 0
resultado = 0
for elemento in final:
    numeros = re.findall(r'[0-9]+',elemento)
    producto = int(numeros[0]) * int(numeros[1])
    i += 1
    resultado += producto
print(resultado)

# Esta parte funciona, falta hacer que se encuentren bien todos los mul(a,b)