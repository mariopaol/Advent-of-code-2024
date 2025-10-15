# Abrimos el fichero input y lo guardamos datos. Como usamos readlines() se guardará como una lista en la que cada elemento es una linea
with open('day2\input.txt','r') as entrada:
    datos = entrada.readlines()

# Variables globales
valida = 0

# La versión anterior del ejercicio no nos sirve para esta segunda parte. Vamos a hacer funciones para resolverlo
# Esta función hace lo que el ejercicio 1. Te dice si una lista es monótona (creciente o decreciente) y sus elementos se alejan como máximo en 3
def report_valido(list):
    crece = 0
    for i in range (len(list)-1):
        if abs(list[i] - list[i+1]) <= 3:
            if list[i] - list[i+1] > 0:
                crece +=1
            elif list[i]-list[i+1] < 0:
                crece -=1
        else:
            break
    if crece == len(list)-1 or crece == -len(list)+1:
        return True

# Eliminamos los elementos de cada report de uno en uno y comprobamos si con ese cambio el report es válido. Esto es el dampener del problema 2
def dampener(list):
    for i in range (len(list)):
        lista_auxiliar = list.copy()
        del lista_auxiliar[i]
        if report_valido(lista_auxiliar) == True:
            return True
        else:
            continue

# Ahora hacemos las llamadas a las funciones
for line in datos:
    report = line.split()   # Separamos en cada espacio. Se guardará como una lista con strings separados por cada espacio
    crece = 0
    for i in range (0,len(report)):     # Este bucle es para convertir los strings en int, así tenemos la lista con valores numéricos
        report[i] = int(report[i])
    if report_valido(report) == True:
        valida += 1
    elif dampener(report) == True:
        valida += 1
    
print(valida)
