# Tomando el método de la parte 1 pero un poco más refinado
with open('2025\\day1\\input.txt','r') as entrada:
    datos = entrada.readlines()

import re


def desp(origen,desplazamiento):
    movimiento = re.split('(\d+)',desplazamiento)
    vueltas = 0
    if 'L' in desplazamiento:
        fin = origen - int(movimiento[1])
        posicion = fin % 100
        vueltas = abs(fin // 100)                
        return (posicion,vueltas)
    if 'R' in desplazamiento:
        fin = origen + int(movimiento[1])
        posicion = fin % 100
        vueltas = abs(fin // 100)  
        return (posicion,vueltas)

origen = 50
contador = 0
for giro in datos:
    aux = desp(origen,giro)
    origen = aux[0]
    contador += aux[1]

print(contador)