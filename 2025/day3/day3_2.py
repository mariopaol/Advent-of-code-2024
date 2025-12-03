with open('2025\\day3\\input.txt','r') as entrada:
    datos = entrada.read().splitlines()

def maximo_string(string,posicion_anterior):
    maximo = 0
    posicion_maximo = 0
    for i in range(len(string)):
        if int(string[i]) > maximo:
            maximo = int(string[i])
            posicion_maximo = i + (posicion_anterior)
    return (maximo,posicion_maximo)


resultado = 0
pilas_usadas = 12
for linea in datos:
    construyendo = 0
    candidato = (0,0) # El primero será el valor del candidato y el segundo la posición

    for i in range(pilas_usadas):
        candidato = maximo_string(linea[candidato[1] + i : len(linea) - pilas_usadas + i + 1], candidato[1])
        construyendo = int( str(construyendo) + str(candidato[0]) )
    resultado += construyendo
    print(construyendo)
print(resultado)