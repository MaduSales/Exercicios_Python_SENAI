idade = int(input('Digite sua idade: '))
doenca = input('Você possui alguma doença pré-existente? Digite "S" para sim e "N" para não: ')
doenca = doenca.upper()

if idade < 18:
    if doenca == 'N':
        mensalidade = 100
    else: 
        mensalidade = 150
elif idade >= 18 and idade <= 59:
    if doenca == 'N':
        mensalidade = 200
    else: 
        mensalidade = 250
else:
    if doenca == 'N':
        mensalidade = 300
    else: 
        mensalidade = 350
60

print(f'A sua mensalidade do plano de saúde é: {mensalidade}')