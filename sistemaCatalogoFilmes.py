filmes = [
    {'nome': 'Indiana Jones', 'genero': 'Aventura', 'disponibilidade': 'Disponível'},
    {'nome': 'Titanic', 'genero': 'Romance', 'disponibilidade': 'Disponível'},
    {'nome': 'Wicked', 'genero': 'Drama', 'disponibilidade': 'Indisponível'},
    {'nome': 'Matrix', 'genero': 'Ficção Científica', 'disponibilidade': 'Disponível'},
    {'nome': 'O Poderoso Chefão', 'genero': 'Drama', 'disponibilidade': 'Disponível'},
    {'nome': 'De Volta para o Futuro', 'genero': 'Aventura', 'disponibilidade': 'Indisponível'},
    {'nome': 'Forrest Gump', 'genero': 'Romance', 'disponibilidade': 'Disponível'},
    {'nome': 'Os Vingadores', 'genero': 'Ação', 'disponibilidade': 'Disponível'},
    {'nome': 'Jurassic Park', 'genero': 'Aventura', 'disponibilidade': 'Indisponível'},
    {'nome': 'Clube da Luta', 'genero': 'Drama', 'disponibilidade': 'Disponível'}
]

def exibir_filmes(filmes):
    i = 0
    print('\n----------------------------')
    print('FILMES')

    for filme in filmes:
        print(f'{i + 1}. {filme['nome']} ({filme['genero']}) - {filme['disponibilidade']}')
        i += 1
    print('----------------------------')



def cadastrar_filme():
    nome = input('Qual o nome do filme? ')
    nome = nome.title()
    for i in range(len(filmes)):
        for filme in filmes:
            while nome.title() == filme['nome'].title():
                nome = input('Esse filme já está cadastrado. Tente novamente ')
                nome = nome.title()

    genero = input('Qual o gênero do filme? ')
    genero = genero.capitalize()
    disponibilidade = 'Disponível'

    novoFilme = {'nome':nome, 'genero':genero, 'disponibilidade':disponibilidade}
    filmes.append(novoFilme)
    print(f'\n" {nome} " foi adicionado com sucesso!')


def consulta_genero():
    i = 0
    encontrado = False
    genero = input('Por qual gênero você gostaria de buscar os filmes? ')
    genero = genero.title()
    print('\n---------------------------------')
    print(f'Filmes do gênero: {genero}')
    for filme in filmes:
        if genero.lower() == filme['genero'].lower():
            print(f'{i+1} -> {filme['nome']} - {filme['disponibilidade']}')
            i += 1
            encontrado = True
    if encontrado == False:
        print('Não há filmes para esse gênero!')
    print('---------------------------------\n')


def alterar_disponibilidade():
    nome = input('Qual filme você gostaria de alterar a disponibilidade? ')
    encontrado = False
    for filme in filmes:
        if nome.title() == filme['nome'].title():
            encontrado = True
            if filme['disponibilidade'].capitalize() == 'Disponível':
                filme['disponibilidade'] = 'Indisponível'
            else: 
                filme['disponibilidade'] = 'Disponível'
            print(f'\nDisponibilidade alterada com sucesso! {filme['nome']} agora está {filme['disponibilidade']}!')
            print('-------------------------------------------------------------\n')
            break 
    if encontrado == False:
        print('Ops... Filme não encontrado!\n') 
        print('---------------------------------\n')



def filtro_genero_disponibilidade():
    i = 0
    encontrado = False
    genero = input('Por qual gênero você gostaria de buscar os filmes? ')
    genero = genero.title()
    print('\n---------------------------------')
    print(f'Filmes atualmente disponíveis do gênero: {genero}')
    for filme in filmes:
        if genero.lower() == filme['genero'].lower() and filme['disponibilidade'].capitalize() == 'Disponível':
            print(f'{i+1} -> {filme['nome']} ({filme['genero']})')
            i += 1
            encontrado = True
    if encontrado == False:
        print('Não há filmes para esse gênero!')
    print('---------------------------------\n')



while True:
    print('\nSeja bem-vindo(a) ao TDSFlix!')
    escolha = input('\nSelecione uma opção:\n1- Ver filmes\n2- Cadastrar filme\n3- Consultar por gênero \n4- Alterar disponibilidade\n5- Filtrar por gênero e disponibilidade \n6- Sair\nInsira: ')
    match escolha:
        case '1':
           exibir_filmes(filmes)
        case '2':
            cadastrar_filme()
        case '3':
            consulta_genero()
        case '4':
            alterar_disponibilidade()
        case '5':
            filtro_genero_disponibilidade()
        case '6':
            print('Até a próxima!')
            break
        case _:
            print('\nOpção inválida. Digite novamente.\n')
