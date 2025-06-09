alunos = ['João', 'Maria', 'José', 'Gabriel']
valor_procurado = 'José'

for aluno in alunos:
    if aluno == valor_procurado:
        print(f'Encontramos o aluno {aluno}.')
        break
    else:
        print(f'Aluno: {aluno}.')