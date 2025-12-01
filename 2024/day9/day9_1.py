#with open('2024\\
# day9\\input.txt','r') as entrada:
    #datos = entrada.readlines()

datos = '2333133121414131402'

# Lo primero es generar el string de archivos y espacio libre
i = 0
ID = 0
cadena = ''
for char in datos:
    if i % 2 == 0:
        cadena = cadena + (int(char) * str(ID))
        ID += 1
    if i % 2 != 0:
        cadena = cadena + (int(char) * '.')
    i += 1

# Ahora tenemos que hacer el algoritmo para ordenar
lista = []
for char in cadena:
    lista.append(char)

contador = 1
for i in range(len(lista)):
    if lista[i] == '.':
        lista[i] = lista[-contador]
        lista[-contador] = '.'
    contador += 1

resultado = ''.join(lista)
print(resultado)
# Por último, hacemos el checksum
checksum = 0
posicion = 0
for char in lista:
    if char == '.':
        continue
    checksum += int(char) * posicion
    posicion += 1

print(checksum)