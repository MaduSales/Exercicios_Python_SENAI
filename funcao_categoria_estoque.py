def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False

produtos = ['BEB4589', 'BEB2019', 'BEB4738', 'BSA1234', 'BSA3984', 'BSA8972']

# Utilizando passagem em ordem
for produto in produtos:
    if categoria(produto, 'BEB'):
        print(f'Enviar {produto} para o setor de bebidas alcoólicas.')
    elif categoria(produto, 'BSA'):
        print(f'Enviar {produto} para o setor de bebidas sem álcool.')

print('\n\n')

# Utilizando uma ordem diferente
for produto in produtos:
    if categoria(cod_categoria='BEB', bebida=produto):
        print(f'Enviar {produto} para o setor de bebidas alcoólicas.')
    elif categoria(cod_categoria='BSA', bebida=produto):
        print(f'Enviar {produto} para o setor de bebidas sem álcool.')
