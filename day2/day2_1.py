# Abrimos el fichero input y lo guardamos datos. Como usamos readlines() se guardará como una lista en la que cada elemento es una linea
with open('day2\input.txt','r') as entrada:
    datos = entrada.readlines()

# Variables globales
valida = 0

for line in datos:
    report = line.split()   # Separamos en cada espacio. Se guardará como una lista con strings separados por cada espacio
    crece = 0
    
    for i in range (len(report)):   # Este bucle es para convertir los strings en int, así tenemos la lista con valores numéricos
        report[i] = int(report[i])
    for i in range (len(report)-1):
        if abs(report[i] - report[i+1]) <= 3:   # Queremos que la diferencia sea como máximo 3, como especifíca el ejercicio
            if report[i] - report[i+1] > 0:     # Si el elemento i+1 es más grande que el i, lo contamos como creciente
                crece +=1
            elif report[i]-report[i+1] < 0:     # Si el elemento i+1 es más pequeño que el i, lo contamos como decreciente
                crece -=1
        else:
            break
        if crece == len(report)-1 or crece == -len(report)+1:   # Necesitamos que toda la lista sea creciente o decreciente para que sea válida. No valen iguales
            valida += 1
print(valida)
