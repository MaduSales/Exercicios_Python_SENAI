import os
sala = 0
horario = 0
reservas = [('Sala 1', '14h'), ('Sala 2', '10h'), ('Sala 3', '11h')]
salas = ['Sala 1', 'Sala 2', 'Sala 3', 'Sala 4']
horarios = ['10h', '11h', '12h', '13h', '14h']



def verificar_disponibilidade(reservas, sala, horario):
        if (sala, horario) in reservas :
            print(f'\nInfelizmente a {sala} já está reservada às {horario}.\n')
       
        else:
            print(f'\n{sala} disponível às {horario}!\n')
    
def adicionar_reserva(reservas, sala, horario):
    if (sala, horario) in reservas :
        print(f'\nInfelizmente a {sala} já está reservada para as {horario}.\n')
    else:
        reservas.append((sala, horario))
        print(f'\nA {sala} foi reservada para as {horario}!\n')

def receber_dados():
    # global sala
    # global horario
    print('\n\nEscolha uma sala: ')
    for i, sala in enumerate(salas):
        print(f'{i + 1} -', sala)
    sala = int(input('Insira: '))
    while sala > 4 or sala < 1:
        sala = int(input('Opção Inválida! Olhe novamente a disponibilidade.'))
    sala = salas[sala - 1]
    print('\n\nEscolha um horário para verificar: ')
    for i, horario in enumerate(horarios):
        print(f'{i + 1} -', horario)
    horario = int(input('Insira: '))
    while horario > 5 or horario < 1:
        horario = int(input('Opção Inválida! Olhe novamente a disponibilidade. '))
    horario = horarios[horario - 1]

while True:
    escolha = input('\nSelecione uma opção:\n1- Adicionar nova reserva\n2- Verificar reservas\n3- Listar reservas\n4- Sair\nInsira: ')
    match escolha:
        case '1':
            os.system('cls')
            receber_dados()
            adicionar_reserva(reservas, sala, horario)
        case '2':
            receber_dados()
            verificar_disponibilidade(reservas, sala, horario)
        case '3':
            print(reservas)
        case '4':
            print('Até a próxima!')
            break
        case _:
            print('\nOpção inválida. Digite novamente.\n')
            continue


# Colocar lista organizada e perguntar se quer resolver
