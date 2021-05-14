# -*- coding: utf-8 -*-

# ZIP compacta as 2 lista como se fosse uma unica lista

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante"]
lista3 = ["R$2,00","R$5,00","Inestimável", "Inestimável","Inestimável"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero , nome, valor)