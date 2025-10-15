with open('day1\input.txt','r') as entrada:
    lineas = entrada.readlines()
x = []
y = []
i = 0
distancia_total = 0

for line in lineas:
    datos = line.split()
    x.append(int(datos[0]))
    y.append(int(datos[1]))

x = sorted(x)
y = sorted(y)

for dato in x:
    distancia = abs(x[i] - y[i])
    distancia_total += distancia
    i += 1

print(distancia_total)