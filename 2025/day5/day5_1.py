with open('2025\\day5\\input.txt','r') as entrada:
    datos = entrada.read().splitlines()

# Guardo los rangos en una lista, y en el mismo bucle puedo trabajar con las ID
rangos = []
fresco = 0
for linea in datos:
    if '-' in linea:
        aux = linea.split('-')
        rangos.append(aux)
    elif linea == '':
        continue
    else: # A partir de aquí las lineas son las ID de productos
        for rango in rangos:
            if int(linea) > int(rango[0]) and int(linea) < int(rango[1]):
                fresco += 1
                break
print(fresco)
