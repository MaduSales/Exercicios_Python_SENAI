estoque = {}

for i in range(5):
    produto = input(f'Digite o nome do item {i + 1}: ')
    quantidade = int(input('Digite a quantidade desse produto em estoque: '))
    estoque[produto] = quantidade

for produto, quantidade in estoque.items():
    if quantidade < 5:
        print(f'\n{produto}:{quantidade}')





