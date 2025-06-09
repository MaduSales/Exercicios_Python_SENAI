
idade = int(input('Digite sua idade: '))

if idade < 18:
    categoria = 'Criança'
elif idade >= 18 and idade <= 59:
    categoria = 'Adulto'
else:
    categoria = 'Idoso'

print(f'Você é classificado como: {categoria}')