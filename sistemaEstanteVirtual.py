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
        "autor": "Emily Brontë",
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
        for i in range(len(livros)):
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
    print(f'\n" {titulo} " foi adicionado com sucesso!')


while True:
    print('\nSeja bem-vindo(a) ao Sistema de Gerenciamento de Livros!')

    # livroAleatorio = input('Você gostaria de uma indicação de leitura? S/N')
    escolha = input('\nSelecione uma opção:\n1- Listar livros do catálogo\n2- Cadastrar Livro\n3- Avaliar um livro\n4- Pesquisar obras por autor\n5- Ver sinopse de um livro\n6- Sair\nInsira: ')
    match escolha:
        case '1':
           listar_livros(livros)
        case '2':
            cadastrar_livro()
        case '3':
            print(9)
        case '4':
            print(9)
        case '5':
            print()
        case '6':
            break
        case _:
            print('\nOpção inválida. Digite novamente.\n')
