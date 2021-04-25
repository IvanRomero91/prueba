numeroSecreto = 777
numeroMuggle = int(input("""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
"""))

while numeroMuggle != numeroSecreto:
     print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
     numeroMuggle = int(input('ingresa un número nuevamente!'))
     if numeroMuggle == numeroSecreto:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break