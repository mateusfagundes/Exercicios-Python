# ELIF Executa a primeira condição verdadeira que encontrar ignorando as demais

x = 1
y = 2

if x == y:
    print("numeros iguais")
elif x < y:
    print ("y menor que x")
elif y > x:
    print ("y maior que x")
else:
    print("numeros diferentes")