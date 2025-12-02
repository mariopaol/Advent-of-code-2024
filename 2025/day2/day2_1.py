with open('2025\\day2\\input.txt','r') as entrada:
    datos = entrada.readlines()
datos_individuales = datos[0].split(',')

resultado = 0

for rango in datos_individuales:
    rango_min = int(rango.split('-')[0])
    rango_max = int(rango.split('-')[1])
    for i in range(rango_min , rango_max + 1):
        if len(str(i)) % 2 != 0:
           continue
        primera_mitad = str(i)[:len(str(i))//2]
        segunda_mitad = str(i)[len(str(i))//2:]
        if primera_mitad == segunda_mitad:
            resultado += i
print(resultado)