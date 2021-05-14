x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2) # Para obter a lista x elevada ao quadrado

print(x)
print(y)

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x] # Para obter a lista x elevada ao quadrado usando list comprehension

print(x)
print(y)

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1] # Nessa condição só são listados os numeros impares

print(z)