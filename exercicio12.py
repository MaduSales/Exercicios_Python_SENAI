faturamento = 0
qtd_mais_vendido = 0

vendas = [
    ("25/11/2024", "Galaxy S24 Ultra", "Preto", "256GB", 400, 7000),
    ("25/11/2024", "Galaxy S24 Ultra", "Rose", "256GB", 200, 7000),
    ("25/11/2024", "IPhone 15 Pro Max", "Preto", "256GB", 350, 9000),
    ("25/11/2024", "IPhone 15 Pro Max", "Preto", "512GB", 250, 14000),
    ("26/11/2024", "Galaxy S24 Ultra", "Preto", "256GB", 317, 7000),
    ("26/11/2024", "Galaxy S24 Ultra", "Rose", "256GB", 212, 7000),
    ("26/11/2024", "IPhone 15 Pro Max", "Preto", "256GB", 150, 9000),
    ("26/11/2024", "IPhone 15 Pro Max", "Preto", "512GB", 50, 14000)
]

for item in vendas:
    data, produto, cor, capacidade, unidades_vendidas, valor_unitario = item

    if data == "25/11/2024" and produto == "IPhone 15 Pro Max":
        faturamento += unidades_vendidas * valor_unitario
    
    if data == "26/11/2024":
        if unidades_vendidas > qtd_mais_vendido:
            produto_mais_vendido = produto
            qtd_mais_vendido = unidades_vendidas

print(f'O faturaento do Iphone Pro Max no dia 25/11/2024 foi de {faturamento:,}')
print(f'O produto mais vendido foi {produto_mais_vendido} com {qtd_mais_vendido} unidades vendidas')

