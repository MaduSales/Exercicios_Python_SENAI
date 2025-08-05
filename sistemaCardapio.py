cardapio = {
    'Hamburguer': 15.90,
    'Pizza': 25.00,
    'Salada': 12.00
}

def mostrar_cardapio(cardapio):
    i = 0
    print('\n----------------------------')
    print('CARDÁPIO')

    # Percorre todas as chaves (item) e valores (preco) do dicionário cardapio, por meio do método .items() 
    # O .items() retorna uma lista de pares (chave e valor)
    for item, preco in cardapio.items():
        print(f'{i + 1}. {item} - R${preco:.2f}')
        i += 1
    print('----------------------------')



def fazer_pedido(cardapio):
    total = 0

    # Lista que armazenará os pedidos do cliente
    pedidos = []

    # Lista de itens sendo criada a partir do dicionário, apenas para armazenar os itens do dicionário
    # O .items() retorna uma lista de pares (chave e valor), ou seja, vuira uma lista de tuplas
    itens = list(cardapio.items())
    while True:
        try:
            pedido = int(input('\nInsira o número do seu pedido: '))
            while pedido > len(cardapio) or pedido < 1:
                pedido = int(input('Opção Inválida! Olhe novamente o cardápio.'))
            

            item, preco = itens[pedido - 1]
            # A variável "pedido" representa a escolha do cliente, numerada a partir de 1 (por exemplo, opção 1, 2, 3...).
            # "Pedido - 1" converte para o índice da lista, que começa do zero.
            # "itens[pedido - 1]" acessa o par (item, preço) correspondente.
            # O código faz o desempacotamento: atribui a primeira parte à variável item (nome) e a segunda à variável preco.
            
            pedidos.append((item, preco))
            # item e preco são adicionados como tupla dentro da lista Pedidos

            total += preco
            # A variável total somará todos os precos dos itens dos pedidos

            print(f'Você adicionou ao carrinho: {item}')
            extra = input('\nDeseja adicionar mais alguma coisa? Digite S ou N: ')
            if extra.upper() == 'S':
                continue
            else:
                break
        except ValueError:
            print('Inválido!')
    return total, pedidos


def exibir_comanda(total, pedidos):
    i = 0
    print('\n----------------------------')
    print('COMANDA')
    print(f'\nVocê pediu: ')
    # Como "Pedidos" é uma lista de tuplas, é possível acessar os valores da tupla apenas com 1 for
    for item, preco in pedidos:
        print(f'{i + 1}. {item} - custou R${preco:.2f}')
        i += 1

    adicional = input('Você deseja deixar 10% de acréscimo para os garçons? Digite S ou N: ')

    if adicional.upper() == 'S':
        gorjeta = total * 0.10
        total_pedido = total + gorjeta
    else:
        total_pedido = total
    print(f'\nO total foi de R${total_pedido:.2f}')
    print('----------------------------')

while True:
    print('\nSeja bem-vindo(a) ao restaurante TDS!')
    escolha = input('\nSelecione uma opção:\n1- Mostrar Cardápio\n2- Fazer pedido\n3- Sair\nInsira: ')
    match escolha:
        case '1':
           mostrar_cardapio(cardapio)
        case '2':
            mostrar_cardapio(cardapio)
            total, pedidos = fazer_pedido(cardapio)
            exibir_comanda(total, pedidos)
        case '3':
            print('Até a próxima!')
            break
        case _:
            print('\nOpção inválida. Digite novamente.\n')
            
