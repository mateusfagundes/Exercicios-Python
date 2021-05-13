w = open("arquivo2.txt", "w")

w.write("Esse e o arquivo 2")

w.close()


w = open("arquivo3.txt", "a") #O "a" é responsável por criar uma linha toda vez que é executato
w.write("Esse e o arquivo 3 \n") #O \n Pula uma linha
w.close()