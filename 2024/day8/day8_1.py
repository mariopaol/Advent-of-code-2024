with open('2024\\day8\\input.txt','r') as entrada:
    datos = entrada.readlines()

'''datos = [
'............',
'........0...',
'.....0......',
'.......0....',
'....0.......',
'......A.....',
'............',
'............',
'........A...',
'.........A..',
'............',
'............'
]'''

def calculo_interferencias(antena1,antena2):
    distanciay = antena1[0] - antena2[0]
    distanciax = antena1[1] - antena2[1]
    interferencia1 = [antena1[0] + distanciay, antena1[1] + distanciax]
    interferencia2 = [antena2[0] - distanciay, antena2[1] - distanciax]
    return [interferencia1,interferencia2]
    

antenas = []
for line in datos:
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
        for counter in range(len(misma_frecuencia) - 1):
            if misma_frecuencia[counter] == elemento:
                continue
            aux = calculo_interferencias(elemento,misma_frecuencia[counter])
            if aux[0][0] in range(len(datos)) and aux[0][1] in range(len(datos)):
                if aux[0] not in interferencias:
                    interferencias.append(aux[0])
            if aux[1][0] in range(len(datos)) and aux[1][1] in range(len(datos)):
                if aux[1] not in interferencias:
                    interferencias.append(aux[1])

resultados = len(interferencias)
print(resultados)