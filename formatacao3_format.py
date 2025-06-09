#TIPOS DE .FORMAT

faturamento = 1000
custo = 500
lucro = faturamento - custo
margem = lucro / faturamento

print('O faturamento da loja foi de R${:.2f} e o lucro foi de R${:.2f}. A margem de lucro é {:.0%}'.format(faturamento, lucro, margem)) 
print(f'O faturamento da loja foi de R${faturamento:.2f} e o lucro foi de R${lucro:.2f}. A margem de lucro é {margem:.0%}')