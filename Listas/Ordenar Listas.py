lista = [123,345,5,72,46,6,7,3,1,7,0]
lista.sort() #SORT ordena a lista em ordem crescente, alterando ela.
print(lista)

lista = [123,345,5,72,46,6,7,3,1,7,0]
lista = sorted(lista) #SORTED retorna uma lista ordenada, sem  alterar a lista.
print(lista)

lista = [123,345,5,72,46,6,7,3,1,7,0]
lista.sort(reverse=True) #SORT(REVERSE=True) ordena a lista em ordem decrescente, alterando ela.
print(lista)

lista = [123,345,5,72,46,6,7,3,1,7,0]
lista.reverse() #Só Inverte a lista do ultimo ao primeiro item
print(lista)


#Usando String
lista2 = ["Fusca","Gol","Opala","Palio"]
lista2.sort()
print(lista2)

lista2 = ["Fusca","Gol","Opala","Palio"]
lista2.sort(reverse=True)
print(lista2)