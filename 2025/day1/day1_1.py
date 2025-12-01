# Esta fue mi primera idea. Como ha funcionado, lo voy a dejar como está
with open('2025\\day1\\input.txt','r') as entrada:
    datos = entrada.readlines()

import re

def desp(origen,desplazamiento):
    movimiento = re.split('(\d+)',desplazamiento)
    if 'L' in desplazamiento:
        fin = origen - int(movimiento[1])
        while fin not in range(100):
            fin += 100
        return fin
    if 'R' in desplazamiento:
        fin = origen + int(movimiento[1])
        while fin not in range(100):
            fin -= 100
        return fin

origen = 50
contador = 0
for giro in datos:
    origen = desp(origen,giro)
    if origen == 0:
        contador += 1

print(contador)