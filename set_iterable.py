cpf_clientes = ['111.111.111-11', '222.222.222-22', '222.222.222-22']

print('Existem {} CPFS na lista. '.format(len(cpf_clientes)))

set_cpf = set(cpf_clientes) # <- Tirou os números repetidos
cpf_unicos = list(set_cpf) # <- Passou a ser uma lista
print(cpf_clientes)
print('Porém, são {} clientes diferentes. '.format(len(cpf_unicos)))