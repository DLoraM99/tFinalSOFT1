import ordenamiento
import randomPaises
import random

"""
nomb = ["Peru", "Argentina", "Brasil", "Mexico", "Estados Unidos"]
oro = [1,2,3,4,5]
plata = [1,2,3,4,5]
bronce = [1,2,3,4,5]
total = [3,6,9,12,15]

ordenamiento.bubbleOro(nomb, oro, plata, bronce, total)

print(nomb)
print(oro)
print(plata)
print(bronce)
print(total)

"""

for i in range(5) :
    cantidad = random.randint(10, 20)

    paises = randomPaises.generarPaises(cantidad)

    print(paises)