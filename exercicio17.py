pessoas = []

for i in range(3):
    pessoa = {}
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))

    pessoas.append(pessoa)


for pessoa in pessoas:
    if pessoa['idade'] > 18:
        print(f'{pessoa['nome']} tem mais de 18 anos.')

