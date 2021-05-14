# -*- coding: utf-8 -*-
#O Código acima é para forçar o python a entender caracteres brasileiros

minha_lista1 = ["abacaxi","Uva","Abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["Uva", 2, 9.89, True]

print(minha_lista1[2]) # Para mostrar 1 item selecionado na lista

for item in minha_lista1: # para listar um item embaixo do outro
    print(item)

tamanho = len(minha_lista1) # Para saber o tamanho da lista usa-se o LEN
print(tamanho)

minha_lista1.append("Limão") # APPEND é para inserir uma nova palavra na lista
print(minha_lista1)

if 3 in minha_lista2: # Para saber se o item esta na lista
    print ("3 está na lista")

del minha_lista1[2:] # Deleta a partir do parametro exigido, nesse caso depois de[2:]
print(minha_lista1)

del minha_lista1[:] # Deleta toda a lista
print(minha_lista1)