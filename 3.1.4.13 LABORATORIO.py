# paso 1
beatles=[]
print("Paso 1:", beatles)

# paso 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Paso 2:", beatles)

# paso 3

cuartoB=input('ingrese el cuarto beatle: ')
beatles.append(cuartoB)
quintoB=input('ingrese el quinto beatle: ')
beatles.append(quintoB)
print("Paso 3:", beatles)

# etapa 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,'Ringo Starr')
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))