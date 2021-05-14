#DEF permite a modularização do código (Bloco de códigos), def é a palavra reservada para a função, só sera executada quando for chamada

def soma (x, y):
    return x + y

def multiplicacao(x, y):
    return x*y

s = soma(2, 3)
print(s)

m = multiplicacao(3,4)
print(m)

print(soma(s, m))