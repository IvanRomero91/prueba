palabraSinVocal = ""
userWord = input('Ingrese una palabra: ').upper()

for letra in userWord:
    #print(letra)
    if letra   == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else: palabraSinVocal += letra #print(letra)
print(palabraSinVocal)