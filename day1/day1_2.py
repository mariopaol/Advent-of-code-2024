with open('adventofcode\day1\input.txt','r') as entrada:
    lineas = entrada.readlines()
x = []
y = []
i = 0
veces = 0
similaridad = 0

for line in lineas:
    datos = line.split()
    x.append(int(datos[0]))
    y.append(int(datos[1]))

x = sorted(x)
y = sorted(y)

for datox in x:
    for datoy in y:
        if datox == datoy:
            veces += 1
        similaridad += (veces*datox)
        veces = 0

print(similaridad)