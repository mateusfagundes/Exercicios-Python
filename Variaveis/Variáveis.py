a = "Olá mundo!"
print(a)

var1 = 1 # variável inteira
var2 = 1.1 # variável float
var3 = " I'm String" #variável string
var4 = True # verdadeiro
var5 = False # falso
PI = 3.14

print(var1)
print(var2)
print(var3)
print(var4)

x = """Transformando Comentário em Variável"""

print(x)

#'Somando' as variaveis

print(x + str(var3)) 
print (f'{var3} {var1 + var2}') # Referenciou os valores e somou

raio = float(input('informe a circunferência:'))
area = PI * raio * raio
print(f'A área da circunferência é {area} m².')
