produtos = []

produto1 = input('Digite o nome do primeiro produto: ')
produto2 = input('Digite o nome do segundo produto: ')
produto3 = input('Digite o nome do terceiro produto: ')

produtos = [produto1, produto2, produto3]
print(' '.join(produtos))

while True:
    try:
        item = input('Escolha qual item deseja remover da lista de compras: ')
        produtos.remove(item)
        print(f'Produto {item} removido com sucesso!')
        print(' '.join(produtos))
        break
    except:
        print(f'Erro! O produto {item} não existe na lista!')
        continue
    
