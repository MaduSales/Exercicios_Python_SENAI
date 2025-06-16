reservas = [('Sala 1', '14h'), ('Sala 2', '10h'), ('Sala 3', '11h')]

def verificar_disponibilidade(reservas, sala, horario):
    for reserva in reservas:
        salaReservada, horarioReservado = reserva

        if salaReservada == sala and horarioReservado == horario:
            return print('\nInfelizmente essa sala já está reservada nesse horário.')
        
    return print('\nSala reservada com sucesso!')
    


# Cria um menu 
sala = input('Selecione uma dessas opções para realizar a sua reserva: \n1- Sala 1\n2- Sala 2\n3- Sala 3\n4- Sala 4\n5- Sala 5\nInsira: ')
match sala:
    case '1':
        sala = 'Sala 1'
    case '2':
        sala = 'Sala 2'
    case '3':
        sala = 'Sala 3'
    case '4':
        sala = 'Sala 4'
    case '5':
        sala = 'Sala 5'
    case _:
        print('Erro! Sala inexistente. ')
        



horario = input('\nPara qual horário gostaria de reservar? Considere a disponibilidade de 1h para as salas: \n1- 10h\n2- 11h\n3- 12h\n4- 13h\n5- 14h\nInsira: ')
match horario:
    case '1':
        horario = '10h'
    case '2':
        horario = '11h'
    case '3':
        horario = '12h'
    case '4':
        horario = '13h'
    case '5':
        horario = '14h'
    case _:
        print('Horário inexistente! ')


verificar_disponibilidade(reservas = reservas, sala = sala, horario = horario)
