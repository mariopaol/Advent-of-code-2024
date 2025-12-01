with open('2024\\day8\\input.txt','r') as entrada:
    datos = entrada.readlines()

# Esta función está modificada para la parte 2, ahora devuelve tantas interferencias como esta parte pide, y ya tiene en cuenta que estén dentro del grid
def calculo_interferencias(antena1,antena2,datos):
    resultado = []
    distanciay = antena1[0] - antena2[0]
    distanciax = antena1[1] - antena2[1]
    interferencia1 = [antena1[0] + distanciay, antena1[1] + distanciax]
    if interferencia1[0] in range(len(datos)) and interferencia1[1] in range(len(datos)):
        resultado.append(interferencia1)
    while (interferencia1[0] + distanciay) in range(len(datos)) and (interferencia1[1] + distanciax) in range(len(datos)):
        interferencia1 = [interferencia1[0] + distanciay, interferencia1[1] + distanciax]
        resultado.append(interferencia1)
    interferencia2 = [antena2[0] - distanciay, antena2[1] - distanciax]
    if interferencia2[0] in range(len(datos)) and interferencia2[1] in range(len(datos)):
        resultado.append(interferencia2)
    while (interferencia2[0] - distanciay) in range(len(datos)) and (interferencia2[1] - distanciax) in range(len(datos)):
        interferencia2 = [interferencia2[0] - distanciay, interferencia2[1] - distanciax]
        resultado.append(interferencia2)
    return resultado
    

antenas = []
for line in datos:
    line = line.rstrip('\n') # Tengo que hacer esto porque si no \n cuenta como antena y el grid es más grande de lo que debería
    for char in line:
        if char != '.':
            if char not in antenas:
                antenas.append(char)
#print(antenas)
interferencias = []

for char in antenas:
    misma_frecuencia = []
    for i in range(len(datos)):
        for j in range(len(datos[i])):
            if char == datos[i][j]:
                misma_frecuencia.append([i,j])
    for elemento in misma_frecuencia:
        if elemento not in interferencias:
            interferencias.append(elemento)
        for counter in range(len(misma_frecuencia)):
            if misma_frecuencia[counter] == elemento:
                continue
            aux = calculo_interferencias(elemento,misma_frecuencia[counter],datos)
            for auxiliar in aux:
                if auxiliar not in interferencias:
                    interferencias.append(auxiliar)

resultados = len(interferencias)
print(interferencias)
print(resultados)