meu_dicionario = {"A":"AMEIXA", "B":"BOLA","C":"CASA"}

print(meu_dicionario)
print(meu_dicionario["A"])
print(meu_dicionario["B"])
print(meu_dicionario["C"])

meu_dicionario = {"A":"AMEIXA", "B":"BOLA","C":"CASA"}

for chave in meu_dicionario: #For para navegar entre os itens 
    print(chave) # Nesse caso só a chave

for chave in meu_dicionario:
    print(meu_dicionario[chave]) # Nesse caso só o nome que contem na chave

for chave in meu_dicionario:
    print(chave + ": "+ meu_dicionario[chave]) # Imprime a Chave, depois ": ", depois o nome do item

for i in meu_dicionario.items(): # O Comando ITEMS(): Converte a lista em conjunto de dados (Tupla)
    print(i)

for i in meu_dicionario.values(): # Retorna somente os valores 
    print(i)

for i in meu_dicionario.keys(): # Retorna somente as chaves 
    print(i)