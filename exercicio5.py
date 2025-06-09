tarefas = []
tarefasConcluidas = []

tarefa1 = input('Insira uma tarefa: ')
tarefa2 = input('Insira outra tarefa: ')

tarefas = [tarefa1, tarefa2]


while True:
    try:
        item = input('\n\nQual tarefa você já concluiu? ')
        tarefas.remove(item)
        tarefasConcluidas.append(item)
        print(f'A tarefa "{item}" foi movida com sucesso para a outra lista!')
        break
    except:
        print(f'Erro! A tarefa "{item}" não existe na lista!')
        continue
    
print('\nTarefas Concluídas: ')
print('\n'.join(tarefasConcluidas), '\n')

print('Tarefas Pendentes: ')
print('\n'.join(tarefas))