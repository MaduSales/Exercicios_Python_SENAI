temperatura = 14
if temperatura >= 25:
    print('Dia quente!')
elif temperatura > 15:
    print('Dia agradável!')
else:
    print('Dia frio!')
# ELIF é a estrutura do ELSE IF

idade = int(input('Digite sua idade: '))

if idade < 13:
    categoria = 'Criança'
elif idade < 18:
    categoria = 'Adolescente'
elif idade < 60:
    categoria = 'Adulto'
else:
    categoria = 'Idoso'

print(f'Você é classificado como: {categoria}')