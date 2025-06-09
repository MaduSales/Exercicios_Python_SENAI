nome1 = input('Digite o nome do primeiro estudante: ')
nota1 = float(input('Digite a nota do estudante: '))

nome2 = input('Digite o nome do segundo estudante: ')
nota2 = float(input('Insira a nota do estudante: '))

nome3 = input('Digite o nome do último estudante: ')
nota3 = float(input('Digite a nota: '))

nomes = [nome1, nome2, nome3]
notas = [nota1, nota2, nota3]

print('Lista de estudantes: ', nomes)
print('Lista de notas respectivas: ', notas)

try:
    nomeIndex = input('Digite o nome de um estudante para atualizar a nota: ')
    var = nomes.index(nomeIndex)

    notaAtualizada = input('Agora insira a nova nota: ')
    notas[var] = notaAtualizada

    print('Lista de estudantes: ', nomes)
    print('Lista de notas atualizada: ', notas)
except:
    print(f'Não localizamos {nomeIndex} na lista de Nomes de Alunos!')
