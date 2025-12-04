with open('2025\\day4\\input.txt','r') as entrada:
    datos = entrada.read().splitlines()

def can_access(rollo,mapa):
    contador = 0
    for vertical in range(-1,2):
        for horizontal in range(-1,2):
            if horizontal == 0 and vertical == 0:
                continue
            if [rollo[0] + vertical , rollo[1] + horizontal] in mapa:
                contador += 1
    if contador < 4:
        return True
    else:
        return False

posiciones = []
for i in range(len(datos)):
    for j in range(len(datos[i])):
        if datos[i][j] == '@':
            posiciones.append([i,j])


antiguo = len(posiciones)
nuevo = 0
resultado = 0
while True:
    recogidas = []
    for elemento in posiciones:
        if can_access(elemento,posiciones) == True:
            resultado += 1
            recogidas.append(elemento)
    for elemento in recogidas:
        if elemento in posiciones:
            posiciones.remove(elemento)
    if len(recogidas) == 0:
        break
    nuevo = len(posiciones)
print(antiguo - nuevo)
