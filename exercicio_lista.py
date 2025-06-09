nome = input('Digite seu nome: ')

try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
except:
    print('Valor inválido')
    
aluno = [nome,[nota1,nota2]]
media = (aluno[1][0]+aluno[1][1])/2

print('A média do aluno {} é {}'.format(aluno[0], media))