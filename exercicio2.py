soma = 0

for i in range(3):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    soma += nota

media = soma / 3

if (media < 5):
    print('Aluno reprovado')
elif (media >= 5 and media <= 6.9):
    print('Aluno em recuperação')
else:
    print('Aluno aprovado!')