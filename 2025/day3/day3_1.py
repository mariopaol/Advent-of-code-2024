with open('2025\\day3\\input.txt','r') as entrada:
    datos = entrada.read().splitlines()

resultado = 0
for linea in datos:
    decenas = 0
    posicion_decenas = 0
    unidades = 0
    for i in range(len(linea) - 1):
        if int(linea[i]) > decenas:
            decenas = int(linea[i])
            posicion_decenas = i
    for j in range(posicion_decenas + 1,len(linea)):
        if int(linea[j]) > unidades:
            unidades = int(linea[j])
    resultado += int( str(decenas) + str(unidades) )
print(resultado)