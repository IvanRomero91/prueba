#Integrantes:
#    BERGAGNA ,Cindy
#    BURGOS, Silvina
#    MOINE, Federico
#    ROMERO, Iván
#    SAM SAM, Emir

bloquesApilados = 0
altura = 0
bloquesIngresados = int(input('Ingrese la cantidad de bloques: '))

while bloquesApilados < bloquesIngresados:
    altura += 1
    bloquesApilados += altura

else: print('la altura de su pirámide es: ',altura)