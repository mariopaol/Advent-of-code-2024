with open('2024\\day5\\input.txt','r') as entrada:
    datos = entrada.readlines()

'''datos = ['47|53',
'97|13',
'97|61',
'97|47',
'75|29',
'61|13',
'75|53',
'29|13',
'97|29',
'53|29',
'61|53',
'97|53',
'61|29',
'47|13',
'75|47',
'97|75',
'47|61',
'75|61',
'47|29',
'75|13',
'53|13',

'75,47,61,53,29',
'97,61,53,29,13',
'75,29,13',
'75,97,47,61,53',
'61,13,29',
'97,13,75,29,47']'''

datos_orden = []

def en_orden(linea,datos):
    for i in range (len(linea) - 1):
        for elemento in datos:
            if linea[i] == elemento[0] and linea[i+1] == elemento[1]:
                if i == len(linea) - 2:
                    return True
            if linea[i] == elemento[1] and linea[i+1] == elemento[0]:
                return False
                
'''def ordenar_linea(linea,datos):
    for elemento in datos:
        if '''

# Esto nos separa la entrada en el orden y en las lineas a comprobar
for linea in datos:
    linea = linea.rstrip()
    if '|' in linea:
            datos_orden.append(linea.split('|'))

def suma_lineas_ordenadas(datos,datos_orden):
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
    return suma

suma = 0
for linea in datos:
    if ',' in linea:
        cambios = 0
        linea = linea.rstrip()
        linea_a_comprobar = linea.split(',')
    #   for i in range(5):
        while(en_orden(linea_a_comprobar,datos_orden)) == False:
            for elemento in datos_orden:
                if elemento[0] not in linea_a_comprobar or elemento[1] not in linea_a_comprobar:
                    continue
                if linea_a_comprobar.index(elemento[0]) > linea_a_comprobar.index(elemento[1]):
                    i0 = linea_a_comprobar.index(elemento[0])
                    i1 = linea_a_comprobar.index(elemento[1])
                    tmp = linea_a_comprobar[i0]
                    linea_a_comprobar[i0] = linea_a_comprobar[i1]
                    linea_a_comprobar[i1] = tmp
                
        suma += int(linea_a_comprobar[len(linea_a_comprobar) // 2])
            
suma -= suma_lineas_ordenadas(datos,datos_orden)
                

print(suma)