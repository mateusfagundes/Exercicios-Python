import random

# Sorteia um numero aleatorio de 0 a 10
numero = random.randint(0,10)
print(numero)

# Sorteia um numero pré definido
random.seed(1)
numero = random.randint(0,10)
print(numero)

# Sorteia um numero da lista aleatoriamente (esse comando só funciona sozinho)
lista = [6,45,9,66]
numero = random.choice(lista)
print(numero)