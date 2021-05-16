x = 10
while x: # Conta do 10 ao 1 depois para o laço
    print(x)
    x -= 1
print('Fim') 

x = 0

while x != -1: # Enquato não for digitado -1 o laço não para de rodar
    x = float(input('Informe o numero ou -1 para sair: '))

print('Fim') 


total = 0
qtde = 0
nota = 0

while nota != -1: # Soma as notas e depois divide quado digitado -1
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota

print(f'A média da turma é: {total / qtde}') # o print(f'uma string {variavel}') irá juntar o valor da variável após o texto uma string.

