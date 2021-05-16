for i in range(10):
    print(i, end=' ')
print(' ')
    

for i in range (1, 11):
    print(i, end=' ')
print(' ')
   

for i in range(4, 100, 7):
    print(i, end=' ')
print(' ')

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=' ')
print(' ')

texto = 'Python'
for letra in texto:
    print(letra, end=' ')
print('')

'''for n in {1, 2, 3, 4, 4, 4}
    print(n, end=' ')
print('')''' # Erro não permite numero duplicado

produtos = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produtos:
    print(atrib, produtos[atrib], end=' ')
print('')

for atrib, valor in produtos.items():
    print(atrib, '==>',valor, end=' ')
print('')
for atrib in produtos.keys():
    print(atrib, end=' ') #END=' ' é para deixar tudo na mesma linha