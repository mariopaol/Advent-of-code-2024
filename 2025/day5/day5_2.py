with open('2025\\day5\\input.txt','r') as entrada:
    datos = entrada.read().splitlines()

rangos = []

for linea in datos:
    if '-' in linea:
        aux = linea.split('-')
        rangos.append(aux)

usado = [0] * len(rangos)
resultado = 0
max = 0
min = 0
j = 0
for i in range(len(rangos)):
    if usado[i] == 1:
        continue
    min = int(rangos[i][0])
    max = int(rangos[i][1])
    j = 0
    while j < len(rangos):
        if usado[j] == 1 or j == i:
            j += 1
            continue
        if int(rangos[j][0]) <= min and int(rangos[j][1]) >= min and int(rangos[j][1]) <= max:
            min = int(rangos[j][0])
            usado[j] = 1
            j = 0
            continue
        if int(rangos[j][0]) >= min and int(rangos[j][0]) <= max and int(rangos[j][1]) >= max:
            max = int(rangos[j][1])
            usado[j] = 1
            j = 0
            continue
        if int(rangos[j][0]) >= min and int(rangos[j][0]) <= max and int(rangos[j][1]) >= min and int(rangos[j][1]) <= max:
            usado[j] = 1
            continue
        if int(rangos[j][0]) <= min and int(rangos[j][1]) >= max:
            min = int(rangos[j][0])
            max = int(rangos[j][1])
            usado[j] = 1
            j = 0
            continue
        j += 1
    usado[i] = 1
    resultado += (max - min + 1)

print(resultado)