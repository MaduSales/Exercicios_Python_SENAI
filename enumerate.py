vendas = [100, 200, 300]
funcionarios = ['João', 'Maria', 'José']

for i, venda in enumerate(vendas):
    #i, venda = item
    #print(item) -> Gera uma tupla com o índice e o item correspondente na lista 'vendas'
    #print(i)
    #print(venda) # Desempacotamento de tuplas com enumerate
    print(f'Funcionário {funcionarios[i]} vendeu {venda}')