nota = float(input('informe a nota do aluno: '))
comportado = True if input('Comportado (s/n): ') == 'y' else False 

if nota >= 9 and comportado:
    print('Excelente')

elif nota >= 7: 
    print('Aprovado')

elif nota >= 5.5: 
    print('Recuperação')

elif nota >= 3.5: 
    print('Recuperação + Trabalho')

else: 
    print('Reprovado')

print(nota)
