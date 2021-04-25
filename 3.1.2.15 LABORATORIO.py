c0= int(input('Ingrese un número natural: '))
pasos= 0

while c0 != 1:
    if c0 <= 0:        #debe ser un valor positivo
        break
        
    elif c0 %2 == 0:   #si c0 es número par
        pasos += 1
        c0 //= 2
        print(c0)

    elif c0 %2 != 0:   #si c0 no es número par
        pasos += 1
        c0= 3*c0+1
        print(c0)

    elif c0 != 1:      #repetir ciclo hasta que c0 == 1
        pasos += 1
        continue

print('Pasos= ',pasos)