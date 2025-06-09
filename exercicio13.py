nomes = []

for i in range(5):
    nome = input(f'Digite o {i + 1}º nome: ')
    nome = nome.lower()
    nomes.append(nome)

for nome in nomes:
    if nome.startswith('a'):
        print(nome.capitalize())
    