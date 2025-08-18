livros = [
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "sinopse": "Em um futuro distópico, Winston Smith luta contra um regime totalitário liderado pelo Grande Irmão.",
        "avaliacoes": [5, 3, 4],
        "media_avaliacao": 4.0,
        "genero": "Ficção Científica",
        "ano": 1949
    },
    {
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "sinopse": "O cavaleiro Don Quixote e seu escudeiro Sancho Pança partem em aventuras, desafiando a realidade em nome da honra.",
        "avaliacoes": [],
        "media_avaliacao": 0,
        "genero": "Romance de Cavaleria",
        "ano": 1605
    },
    {
        "titulo": "Frankenstein",
        "autor": "Mary Shelley",
        "sinopse": "Victor Frankenstein cria um monstro, que busca vingança após ser rejeitado por seu criador.",
        "avaliacoes": [5, 5],
        "media_avaliacao": 5.0,
        "genero": "Gótico",
        "ano": 1818
    },
    {
        "titulo": "O Grande Gatsby",
        "autor": "F. Scott Fitzgerald",
        "sinopse": "Jay Gatsby, um milionário misterioso, tenta reconquistar o amor perdido de Daisy Buchanan nos anos 1920.",
        "avaliacoes": [4, 3],
        "media_avaliacao": 3.5,
        "genero": "Romance",
        "ano": 1925
    },
    {
        "titulo": "Tender Is the Night",
        "autor": "F. Scott Fitzgerald",
        "sinopse": "A história de um casal em decadência durante a década de 1920, explorando temas de amor, traição e destruição pessoal.",
        "avaliacoes": [4],
        "media_avaliacao": 4.0,
        "genero": "Romance",
        "ano": 1934
    },
    {
        "titulo": "O Morro dos Ventos Uivantes",
        "autor": "Emily Bronte",
        "sinopse": "A história de amor obsessivo entre Heathcliff e Catherine, marcada por vingança e sofrimento.",
        "avaliacoes": [],
        "media_avaliacao": 0,
        "genero": "Romance Gótico",
        "ano": 1847
    }
]




def listar_livros(livros):
    i = 0
    print('\n-----------------------------------------------------')
    print('LIVROS NO CATÁLOGO\n')

    for livro in livros:
        print(f'{i + 1}. {livro['titulo']} ({livro['ano']}) - Autor(a): {livro['autor']} - {livro['genero']}\n')
        i += 1
    print('-------------------------------------------------------')


def cadastrar_livro():
    try:
        titulo = input('Qual o nome do livro? ').title()
        for livro in livros:
            while titulo == livro['titulo'].title():
                titulo = input('Esse livro já está cadastrado. Tente cadastrar outro livro. ').title()

        autor = input('Quem escreveu o livro? ').title()

        genero = input('Qual o gênero do livro? ').capitalize()

        ano = int(input('Qual o ano de lançamento do livro? '))
        while len(str(ano)) != 4:
            ano = int(input('Digite um ano válido de quatro dígitos: '))


        sinopse = input('Digite uma breve sinopse para o livro: ').capitalize() 
            
        while not sinopse.strip(): # Verifica se a sinopse não está vazia
                sinopse = ('Escreva algo para ser mostrado como sinopse do livro adicionado: ').capitalize()

        avaliacoes = []
        media_avaliacoes = 0.0
    
    except ValueError:
        print('Erro de caractere!')

    novoLivro = {'titulo':titulo, 'autor':autor, 'sinopse':sinopse, 'avaliacoes':avaliacoes, 'media_avaliacoes':media_avaliacoes, 'genero':genero, 'ano':ano}
    livros.append(novoLivro)
    print(f'\n {titulo} foi adicionado com sucesso!')


def avaliar_livro():
    try:
        titulo = input('\nQual o nome do livro? ').title()
        encontrado = False
        for livro in livros:
            if titulo == livro['titulo'].title():
                encontrado = True
                break
        if encontrado == False:
            titulo = input('Não foi possível encontrar esse livro... Tente buscar por algum que esteja no catálogo. ').title()
        
        print(f'\nMédia de avaliações atualmente para este livro: {livro['media_avaliacao']:.1f}')
        nota = float(input(f'De 0 a 5, qual a sua nota para {titulo}? '))
        while (nota < 0 or nota > 5):
            nota = float(input(f'Tente novamente... De 0 a 5, qual a sua nota para {titulo}? '))

        livro['avaliacoes'].append(nota)
        livro['media_avaliacao'] = sum(livro['avaliacoes']) / len(livro['avaliacoes'])
        print(f'\nNova avaliação para {titulo} cadastrada!\nMédia de avaliações atualmente para este livro: {livro['media_avaliacao']:.1f}')

    except ValueError:
        print('Erro de caractere!')


def listar_avaliacoes():
    while True:
        i = 0
        print('\n-----------------------------------------------------')
        print('AVALIAÇÕES DO CATÁLOGO\n')

        for livro in livros:
            print(f'{i + 1}. {livro['titulo']} - {livro['media_avaliacao']}')
            i += 1
        print('-------------------------------------------------------')

        avaliar = input('Gostaria de avaliar um livro? Responda S para "Sim", ou qualquer outra tecla para "Não": ').upper()
        if avaliar == 'S':
            avaliar_livro()
            break
        else:
            break


def pesquisar_autor():
    i = 0
    encontrado = False
    autor = input('Por qual autor você gostaria de buscar os livros? ').title()
    print('\n---------------------------------')
    print(f'Livros do autor: {autor}')
    for livro in livros:
        if autor == livro['autor'].title():
            print(f'{i+1} -> {autor} - {livro["titulo"]}')
            i += 1
            encontrado = True
    if encontrado == False:
        print('Não há livros cadastrados para esse autor!')
    print('---------------------------------\n')



while True:
    print('\nSeja bem-vindo(a) à Estante Virtual de Livros!')

    # livroAleatorio = input('Você gostaria de uma indicação de leitura? S/N')
    escolha = input('\nSelecione uma opção:\n1- Listar livros do catálogo\n2- Cadastrar Livro\n' \
    '3- Avaliar um livro\n4- Listar avaliações dos livros em catálogo\n5- Pesquisar obras por autor\n' \
    '6- Ver sinopse de um livro\n7- Sair\nInsira: ')
    match escolha:
        case '1':
           listar_livros(livros)
        case '2':
            cadastrar_livro()
        case '3':
            avaliar_livro()
        case '4':
            listar_avaliacoes()
        case '5':
            pesquisar_autor()
        case '6':
            print(3)
        case '7':
            break
        case _:
            print('\nOpção inválida. Digite novamente.\n')
