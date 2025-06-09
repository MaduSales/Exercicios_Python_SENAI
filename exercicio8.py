vendas = [50, 100, 200, 300, 400, 500]
meta = 300
qtd_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtd_bateu_meta += 1
    
print(qtd_bateu_meta , 'funcionários bateram a meta')
qtd_funcionarios = len(vendas)
print('O percentual de funcionários que bateram a meta foi de: {:.2%}'.format(qtd_bateu_meta/qtd_funcionarios))