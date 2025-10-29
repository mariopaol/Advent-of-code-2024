#with open('day6\\input.txt','r') as entrada:
    #datos = entrada.readlines()

datos = ['....#.....',
'.........#',
'..........',
'..#.......',
'.......#..',
'..........',
'.#..^.....',
'........#.',
'#.........',
'......#...']

# El código de returns será este.
# 0 - Obstáculo, el guardia gira 90º a la derecha
# 1 - El guardia se mueve
# 2 - El guardia sale del grid, terminando el ejercicio
# Por como se leen los datos, las coordenadas son: datos[ejey][ejex]

def arriba(guardia,datos,i,j):
    if guardia[0] - 1 < 0:
        return 2
    if datos[guardia[0] - 1][guardia[1]] == '#' or datos[guardia[0] - 1][guardia[1]] == [i,j]:
        return 0
    else:
        return 1
    
def abajo(guardia,datos,i,j):
    if guardia[0] + 1 >= len(datos):
        return 2
    if datos[guardia[0] + 1][guardia[1]] == '#' or datos[guardia[0] + 1][guardia[1]] == [i,j]:
        return 0
    else:
        return 1
    
def izquierda(guardia,datos,i,j):
    if guardia[1] - 1 < 0:
        return 2
    if datos[guardia[0]][guardia[1] - 1] == '#' or datos[guardia[0]][guardia[1] - 1] == [i,j]:
        return 0
    else:
        return 1
    
def derecha(guardia,datos,i,j):
    if guardia[1] + 1 >= len(datos[0]):
        return 2
    if datos[guardia[0]][guardia[1] + 1] == '#' or datos[guardia[0]][guardia[1] + 1] == [i,j]:
        return 0
    else:
        return 1


# En esta parte del programa guardamos la posición del guardia. Los bucles solo funcionan así si el grid es cuadrado
for i in range(len(datos)):
    for j in range(len(datos[i])):
        if datos[i][j] == '^':
            start = [i,j]


bucles_infinitos = 0

for i in range (len(datos)):
    for j in range(len(datos[0])):
        guardia = start.copy()
        direccion = 'up'
        posiciones_ocupadas = []
        while True:
            print(str(guardia)+direccion)
            print([i,j])
            if (str(guardia)+direccion) in posiciones_ocupadas:
                    bucles_infinitos += 1
                    break
            
            if direccion == 'up':
                if arriba(guardia,datos,i,j) == 0:
                    direccion = 'right'
                elif arriba(guardia,datos,i,j) == 1:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    guardia[0] = guardia[0] - 1
                elif arriba(guardia,datos,i,j) == 2:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    break

            elif direccion == 'down':
                if abajo(guardia,datos,i,j) == 0:
                    direccion = 'left'
                elif abajo(guardia,datos,i,j) == 1:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    guardia[0] = guardia[0] + 1
                elif abajo(guardia,datos,i,j) == 2:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    break

            elif direccion == 'left':
                if izquierda(guardia,datos,i,j) == 0:
                    direccion = 'up'
                elif izquierda(guardia,datos,i,j) == 1:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    guardia[1] = guardia[1] - 1
                elif izquierda(guardia,datos,i,j) == 2:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    break

            elif direccion == 'right':
                if derecha(guardia,datos,i,j) == 0:
                    direccion = 'down'
                elif derecha(guardia,datos,i,j) == 1:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    guardia[1] = guardia[1] + 1
                elif derecha(guardia,datos,i,j) == 2:
                    posiciones_ocupadas.append(str(guardia)+direccion)
                    break

        posiciones_unicas = []
        for elemento in posiciones_ocupadas:
            if elemento not in posiciones_unicas:
                posiciones_unicas.append(elemento)

print(bucles_infinitos)
