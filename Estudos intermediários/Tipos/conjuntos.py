print({1, 2, 3})
print(type({1, 2, 3}))
print({1, 2, 3, 3, 3, 3}) #Não aceita elementos duplicados

conj = {1, 2, 3, 3, 3, 3}
#print(conj[1]) #Da erro pois diferente da tupla ele não aceita valores indexado

print(len(conj)) #Só mostra os elementos não duplicados