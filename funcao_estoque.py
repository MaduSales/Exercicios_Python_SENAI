def com_alcool(bebida):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False

produtos = ['BEB4589', 'BEB2019', 'BEB4738', 'BSA1234', 'BSA3984', 'BSA8972']

for produto in produtos:
    if com_alcool(produto):
        print(f'Enviar {produto} para o setor de bebidas alcoólicas.')