produtos = ['Coca', 'Pepsi', 'Guaraná']
producao = [15000, 10000, 14000]

tamanho = len(produtos)

# for i in range(tamanho):
#     print(f'A produção de {produtos[i]} é de {producao[i]}')


'''ESTRUTURA FOREACH'''
for produto in produtos:
    i = produtos.index(produto)
    print(f'Produção de {produto} é de {producao[i]}')