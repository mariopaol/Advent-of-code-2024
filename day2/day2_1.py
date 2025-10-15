with open('day2\input.txt','r') as entrada:
    datos = entrada.readlines()

crece = 0
valida = 0

for line in datos:
    report = line.split()
    #print(report)
    crece = 0
    for i in range (len(report)):
        report[i] = int(report[i])
    for i in range (len(report)-1):
        if abs(report[i] - report[i+1]) <= 3:
            if report[i] - report[i+1] > 0:
                crece +=1
            elif report[i]-report[i+1] < 0:
                crece -=1
        else:
            #print('Hay una diferencia mayor que 3.')
            break
        #print(crece)
        if crece == len(report)-1 or crece == -len(report)+1:
            #print('línea válida')
            valida += 1
print(valida)
