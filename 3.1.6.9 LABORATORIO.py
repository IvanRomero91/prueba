miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#
miLista2 = miLista[:]
miLista.sort()

flag=False

for i in miLista:
    flag= miLista[i] in miLista2
    if flag==True:
        del miLista2[i:i+1]
        flag=False
    else: miLista2.append(miLista[i])

#
print("La lista solo con elementos únicos:")
print(miLista2)
