#1 Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

idade = int(input("Digite a idade: "))

resultado = (idade)
print(resultado)
if resultado >= 18 :
    print("Maior de idade")
else:
    print("Menor de idade")
    
#2Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

nota1 = int(input("Digite a primeira nota: "))

nota2 = int(input("Digite a segunda nota: "))

resultado = (nota1 + nota2) /2
print(resultado)
if resultado >= 6 :
    print("Aprovado")
else:
    print("Reprovado")

#3 Escreva um programa que resolva uma equação de segundo grau. 

import math

a = float(input("Insira um valor para A: "))
b = float(input("Insira um valor para B: "))
c = float(input("Insira um valor para C: "))

d = b ** 2 - 4 * a * c
print("Delta: ", d)


if d > 0:
    delta = math.sqrt(d)
    print("Raiz quadrada de delta: ", delta)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print("X1 = ", x1, "X2 = ", x2)

elif d == 0:
    delta = math.sqrt(d)
    print("Raiz quadrada de delta: ", delta)
    x = -b / (2 * a)
    print("Valor de x = ", x)

elif d < 0:
    print("Essa raiz é menor do que zero")

#4 Escreva um programa que ordene uma lista numérica com três elementos. 

lista = [123,345,5]
lista.sort() 
print(lista)

#5 Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 

num1 = float(input("Informe o 1º número: "))
sinal = input("Informe o tipo de operação ( * / + - )")
num2 = float(input("Informe o 2º número: "))
 
if sinal == "*":
  print(num1 * num2)
elif sinal == "/":
  print(num1 / num2)
elif sinal == "+":
  print(num1 + num2)
else:
  print(num1 - num2)