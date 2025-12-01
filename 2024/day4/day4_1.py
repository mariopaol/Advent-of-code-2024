with open('2024\\day4\\input.txt','r') as entrada:
    datos = entrada.readlines()


def checkderecha(coordx,coordy,lista):
    if lista[coordy][coordx + 1] == 'M' and lista[coordy][coordx + 2] == 'A' and lista[coordy][coordx + 3] == 'S':
        return True
def checkizquierda(coordx,coordy,lista):
    if lista[coordy][coordx - 1] == 'M' and lista[coordy][coordx - 2] == 'A' and lista[coordy][coordx - 3] == 'S':
        return True
def checkarriba(coordx,coordy,lista):
    if lista[coordy - 1][coordx] == 'M' and lista[coordy - 2][coordx] == 'A' and lista[coordy - 3][coordx] == 'S':
        return True
def checkabajo(coordx,coordy,lista):
    if lista[coordy + 1][coordx] == 'M' and lista[coordy + 2][coordx] == 'A' and lista[coordy + 3][coordx] == 'S':
        return True
def checktopleft(coordx,coordy,lista):
    if lista[coordy - 1][coordx - 1] == 'M' and lista[coordy - 2][coordx - 2] == 'A' and lista[coordy - 3][coordx - 3] == 'S':
        return True
def checktopright(coordx,coordy,lista):
    if lista[coordy - 1][coordx + 1] == 'M' and lista[coordy - 2][coordx + 2] == 'A' and lista[coordy - 3][coordx + 3] == 'S':
        return True
def checkbottomleft(coordx,coordy,lista):
    if lista[coordy + 1][coordx - 1] == 'M' and lista[coordy + 2][coordx - 2] == 'A' and lista[coordy + 3][coordx - 3] == 'S':
        return True
def checkbottomright(coordx,coordy,lista):
    if lista[coordy + 1][coordx + 1] == 'M' and lista[coordy + 2][coordx + 2] == 'A' and lista[coordy + 3][coordx + 3] == 'S':
        return True

palabras_encontradas = 0
linea = 0
for line in datos:
    posicion_caracter = 0
    for char in line:
        if char == 'X':
            posicion_caracter = line.find(char,posicion_caracter) # Esto nos encuentra todas las X del texto, y tenemos la coordenada X en posicion_caracter y la coordenada y en linea
            if posicion_caracter <= len(line) - 4:
                if checkderecha(posicion_caracter,linea,datos) == True:
                    palabras_encontradas += 1
                if linea <= len(datos) - 4:
                    if checkbottomright(posicion_caracter,linea,datos) == True:
                        palabras_encontradas += 1
                if linea >= 3:
                    if checktopright(posicion_caracter,linea,datos) == True:
                        palabras_encontradas += 1
            if posicion_caracter >= 3:
                if checkizquierda(posicion_caracter,linea,datos) == True:
                    palabras_encontradas += 1
                if linea <= len(datos) - 4:
                    if checkbottomleft(posicion_caracter,linea,datos) == True:
                        palabras_encontradas += 1
                if linea >= 3:
                    if checktopleft(posicion_caracter,linea,datos) == True:
                        palabras_encontradas += 1
            if linea <= len(datos) - 4:
                if checkabajo(posicion_caracter,linea,datos) == True:
                    palabras_encontradas += 1
            if linea >= 3:
                if checkarriba(posicion_caracter,linea,datos) == True:
                    palabras_encontradas += 1
            posicion_caracter += 1
    linea += 1
print(palabras_encontradas)