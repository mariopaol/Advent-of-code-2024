with open('2024\\day5\\input.txt','r') as entrada:
    datos = entrada.readlines()

# Esta versión del programa sólo funciona si TODOS los pares de páginas están en las instrucciones.

datos_orden = []

# Esto nos separa la entrada en el orden y en las lineas a comprobar
for linea in datos:
    linea = linea.rstrip()
    if '|' in linea:
            datos_orden.append(linea.split('|'))

found = False
suma = 0
for linea in datos:
    if ',' in linea:
        found = False
        linea = linea.rstrip()
        linea_a_comprobar = linea.split(',')
        for i in range (len(linea_a_comprobar) - 1):
            for elemento in datos_orden:
                if linea_a_comprobar[i] == elemento[0] and linea_a_comprobar[i+1] == elemento[1]:
                    if i == len(linea_a_comprobar) - 2:
                        suma += int(linea_a_comprobar[(i + 1) // 2]) # si el bucle ha acabado significa que la línea es válida, luego puedo sumarle ahora el elemento central.
                if linea_a_comprobar[i] == elemento[1] and linea_a_comprobar[i+1] == elemento[0]:
                    found = True
                    break
            if found:
                break
                     
print(suma)
datos.sort()
print("\n".join(datos))