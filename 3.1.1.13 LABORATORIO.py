año = int(input("Introduzca un año:"))

if año <= 1582:
    print('No dentro del período del calendario gregoriano')
elif año%4 == 0:
    print('Año bisiesto')
elif año%4 != 0:
    print('Año común')