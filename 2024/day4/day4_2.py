with open('2024\\day4\\input.txt','r') as entrada:
    datos = entrada.readlines()

def checkd1(coordx,coordy,lista):
    if lista[coordy - 1][coordx - 1] == 'M' and lista[coordy + 1][coordx + 1] == 'S':
        return True
    if lista[coordy - 1][coordx - 1] == 'S' and lista[coordy + 1][coordx + 1] == 'M':
        return True

def checkd2(coordx,coordy,lista):
    if lista[coordy - 1][coordx + 1] == 'M' and lista[coordy + 1][coordx - 1] == 'S':
        return True
    if lista[coordy - 1][coordx + 1] == 'S' and lista[coordy + 1][coordx - 1] == 'M':
        return True


equis_encontradas = 0
linea = 0
for line in datos:
    posicion_caracter = 0
    for char in line:
        if char == 'A':
            posicion_caracter = line.find(char,posicion_caracter) # Esto nos encuentra todas las X del texto, y tenemos la coordenada X en posicion_caracter y la coordenada y en linea
            if posicion_caracter in range(1, len(line) - 1) and linea in range(1, len(datos) - 1):
                print(len(line))
                if checkd1(posicion_caracter,linea,datos) == True and checkd2(posicion_caracter,linea,datos) == True:
                    equis_encontradas += 1
                    
            posicion_caracter += 1
    linea += 1
print(equis_encontradas)