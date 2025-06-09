venda = input('Digite o nome do produto e tecle enter para registrar. Para cancelar, tecle enter sem digitar nada.')
vendas = []

while venda != ' ':
    vendas.append(venda)
    venda = input('Digite o nome do produto e tecle enter para registrar. Para cancelar, tecle enter sem digitar nada.')

print(f'Registros finalizados. As vendas foram: {vendas}')