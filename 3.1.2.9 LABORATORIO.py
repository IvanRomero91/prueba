
palabraSecreta = ('chupacabra')
palabra = input('Ingresa la palabra secreta:')

while palabra != palabraSecreta:
    palabra=input('Ingresa la palabra secreta:')
    if palabra == palabraSecreta:
        print('¡Has dejado el ciclo con éxito!')
        break