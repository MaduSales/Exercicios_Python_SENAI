# vendas = [10, 20, 30, 40, 50]

# print(len(vendas))
# print(max(vendas))
# print(min(vendas))

produto_galpao1 = ['tv', 'celular']
produto_galpao2 = ['mouse', 'teclado']

produto_galpao1.extend(produto_galpao2)

print(produto_galpao1) # Extendeu a lista produto_galpao1 adicionando os produtos de produto_galpao2. Mas não modificou a lista 2.




produtos = ['tv', 'celular', 'notebook', 'Mouse', 'teclado']
vendas = [1000, 1500, 2000, 300, 350]

produtos.sort() # Coloca os itens em ordem alfabética e coloca palavras com letras maiúsculas como prioridade
print(produtos)

vendas.sort(reverse=True) # Organiza do maior para o menor
print(vendas)

print(' '.join(produtos)) # Maneira de mostrar lista sem a formatação de lista -> ['1', '2', '3']

