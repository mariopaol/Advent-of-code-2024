# Una forma a lo bruto, pero funciona correctamente
with open('2025\\day1\\input.txt','r') as entrada:
    datos = entrada.readlines()

import re

posicion = 50
contador = 0
for giro in datos:
    movimiento = re.split('(\d+)',giro)

    if 'R' in giro:
        for i in range(int(movimiento[1])):
            if posicion == 0:
                contador += 1
            posicion += 1
            if posicion == 100:
                posicion = 0
    if 'L' in giro:
        for i in range(int(movimiento[1])):
            if posicion == 0:
                contador += 1
            posicion -= 1
            if posicion == -1:
                posicion = 99
print(contador)