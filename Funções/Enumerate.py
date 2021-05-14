lista = ["abacate","bola","cachorro"] 
for i in range(len(lista)): # RENGE cria um vetor e LEN mede o tamanho da lista
    print(i, lista[i])

#Enumerate:

lista = ["abacate","bola","cachorro"] 
for i, nome in enumerate(lista): # Melhor forma de se fazer
    print(i, nome)
