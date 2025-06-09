estoque = [1500, 100, 200, 50, 87]
produtos = ['Coca', 'Pepsi', 'Dolly', 'Café', 'Guaraná']
nivel_minimo = 300

for i, qtd in enumerate(estoque):
    if qtd < nivel_minimo:
        print(f'O produto {produtos[i]} está com o nível baixo: {qtd} unidades.')