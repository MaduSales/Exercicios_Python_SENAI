# Como executar no powershell: python nome_no_arquivo.py
# Em divisões, o resultado sempre será decimal. Caso um dos valores de uma multiplicação seja decimal, o resultado também será decimal.

print('Mariano')
print('Ferraz')

print('Mariano' + 'Ferraz')
print('Mariano','Ferraz') # O uso de vírgula para concatenar strings já coloca um espaço entre as strings

# CASTING
num = '10'
print(num)
print(num + num)

num_int = int(num)
print(num_int)
print(num_int + num_int)

faturamento = 1000
print(type(faturamento)) # Mostra tipo do dado

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print('Seu nome é' , nome , 'e sua idade é' , idade , 'anos.')

print(dir(str))
var = 'stringaa'
print(var[3])

print(len(var))

custo = 500
print('O faturamento da loja foi de R$' + str(faturamento)) # Converteu temporariamente o dado para string
print('O faturamento da loja foi de R$ {} e o custo foi de R${}'.format(faturamento, custo)) 

