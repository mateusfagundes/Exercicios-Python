a = "Brasil"  
b = "China"

concatenar = a + " " + b + "\n" #"\n" pula uma linha, para remover tem que usar print(concatenar.STRIP()).
print(concatenar) 

print(concatenar.lower()) #Método para deixar os caracteres em minúsculo sem alterar a variável

print(concatenar.upper()) #Método para deixar os caracteres em maiúsculo sem alterar a variável

concatenar = concatenar.upper #Método para deixar os caracteres em maiúsculo alterando a variável

#Usando SPLIT
minha_string = "O rato roeu a roupa do rei de Roma"
Minha_lista = minha_string.split()
print(Minha_lista)

#Remover letra com a letra desejada
minha_string = "O rato roeu a roupa do rei de Roma"
Minha_lista = minha_string.split("r") # "r" é a letra a ser removida
print(Minha_lista)

#Busca de String FIND
minha_string = "O rato roeu a roupa do rei de Roma"
busca = minha_string.find("rei") #Buscou onde começa da palavra "rei"
print(busca)

print(minha_string[busca:]) #Para imprimir a frase até o final

minha_string2 = "O rato roeu a roupa do rei de Roma"
minha_string2 = minha_string2.replace("o rei","a rainha")#Subistituir a palavra
print(minha_string2)