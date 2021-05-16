pessoas = ['Gui','Rebeca']
adjs = ['Sapeca','Inteligente']

for p in pessoas: # Liga p a pessoas
    for a in adjs: # liga a a adjs
        print(f'{p} é {a}!') # Concatena tudo

for i in [1, 2, 3]:
    pass # Classe vazia

for i in range(1, 11):
    if i %2: # Vai mostrar somente os valores pares
        continue # Interrompe a repetição e vai para a proxima
    print(i, end=' ')
print('')

for i in range(1,11):
    if i == 5:
        break #  Para a repetição e sai do laço
    print(i, end=' ')
print('Fim!')
