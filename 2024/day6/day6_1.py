with open('2024\\day6\\input.txt','r') as entrada:
    datos = entrada.readlines()

'''datos = ['....#.....',
'.........#',
'..........',
'..#.......',
'.......#..',
'..........',
'.#..^.....',
'........#.',
'#.........',
'......#...']'''

# El código de returns será este.
# 0 - Obstáculo, el guardia gira 90º a la derecha
# 1 - El guardia se mueve
# 2 - El guardia sale del grid, terminando el ejercicio
# Por como se leen los datos, las coordenadas son: datos[ejey][ejex]

def arriba(guardia,datos):
    if guardia[0] - 1 < 0:
        return 2
    if datos[guardia[0] - 1][guardia[1]] == '#':
        return 0
    else:
        return 1
    
def abajo(guardia,datos):
    if guardia[0] + 1 >= len(datos):
        return 2
    if datos[guardia[0] + 1][guardia[1]] == '#':
        return 0
    else:
        return 1
    
def izquierda(guardia,datos):
    if guardia[1] - 1 < 0:
        return 2
    if datos[guardia[0]][guardia[1] - 1] == '#':
        return 0
    else:
        return 1
    
def derecha(guardia,datos):
    if guardia[1] + 1 >= len(datos[0]):
        return 2
    if datos[guardia[0]][guardia[1] + 1] == '#':
        return 0
    else:
        return 1


# En esta parte del programa guardamos la posición del guardia. Los bucles solo funcionan así si el grid es cuadrado
for i in range(len(datos)):
    for j in range(len(datos[i])):
        if datos[i][j] == '^':
            guardia = [i,j]

terminado = False
direccion = 'up'
posiciones_ocupadas = []

while terminado != True:
    if direccion == 'up':
        if arriba(guardia,datos) == 0:
            direccion = 'right'
        elif arriba(guardia,datos) == 1:
            posiciones_ocupadas.append(str(guardia))
            guardia[0] = guardia[0] - 1
        elif arriba(guardia,datos) == 2:
            posiciones_ocupadas.append(str(guardia))
            terminado = True
            break

    elif direccion == 'down':
        if abajo(guardia,datos) == 0:
            direccion = 'left'
        elif abajo(guardia,datos) == 1:
            posiciones_ocupadas.append(str(guardia))
            guardia[0] = guardia[0] + 1
        elif abajo(guardia,datos) == 2:
            posiciones_ocupadas.append(str(guardia))
            terminado = True
            break

    elif direccion == 'left':
        if izquierda(guardia,datos) == 0:
            direccion = 'up'
        elif izquierda(guardia,datos) == 1:
            posiciones_ocupadas.append(str(guardia))
            guardia[1] = guardia[1] - 1
        elif izquierda(guardia,datos) == 2:
            posiciones_ocupadas.append(str(guardia))
            terminado = True
            break

    elif direccion == 'right':
        if derecha(guardia,datos) == 0:
            direccion = 'down'
        elif derecha(guardia,datos) == 1:
            posiciones_ocupadas.append(str(guardia))
            guardia[1] = guardia[1] + 1
        elif derecha(guardia,datos) == 2:
            posiciones_ocupadas.append(str(guardia))
            terminado = True
            break

resultado = []
for elemento in posiciones_ocupadas:
    if elemento not in resultado:
        resultado.append(elemento)

print(len(resultado))
