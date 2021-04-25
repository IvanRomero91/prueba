listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1:solicite al usuario un entero para reemplazar el número de el medio.
listaSombrero[2]=int(input('Ingrese un N° entero: '))
# Paso 2: elimine el último elemento de la lista.
del listaSombrero[-1]
# Paso 3: imprima la longitud de la lista existente.
len(listaSombrero)

print(listaSombrero)