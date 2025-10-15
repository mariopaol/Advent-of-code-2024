with open('adventofcode\day2\input.txt','r') as entrada:
    datos = entrada.readlines()

valida = 0
# Vamos a probar a sacar los elementos 1 a 1 a ver si con eso se soluciona el error. Para ello vamos a hacer una función

# Esta función está probada y ya funciona correctamente
def report_valido(list):
    crece = 0
    for i in range (len(list)-1):
        if abs(list[i] - list[i+1]) <= 3:
            if list[i] - list[i+1] > 0:
                crece +=1
            elif list[i]-list[i+1] < 0:
                crece -=1
        else:
            break
    if crece == len(list)-1 or crece == -len(list)+1:
        return True

# Vamos a hacer que funcione esta otra función
def dampener(list):
    for i in range (len(list)):
        lista_auxiliar = list.copy()
        del lista_auxiliar[i]
        if report_valido(lista_auxiliar) == True:
            return True
            break
        else:
            continue



for line in datos:
    report = line.split()
    crece = 0
    for i in range (0,len(report)):
        report[i] = int(report[i])
    if report_valido(report) == True:
        valida += 1
    elif dampener(report) == True:
        valida += 1
    
print(valida)

