numeros = []
soma = 0
media = 0
maiores_que_media = 0
maiorNumero = 0
menorNumero = 0

for i in range(6):
    numero = float(input(f'Digite o {i + 1}º número: '))
    numeros.append(numero)

print(f'\nLista original: {numeros}')

for numero in numeros:
    soma += numero
media = soma/6

print(f'A média dos números é: {media}')

for numero in numeros:
    if numero > media:
        maiores_que_media += 1

print(f'{maiores_que_media} números são maiores do que a média')

maiorNumero = max(numeros)
menorNumero = min(numeros)

print(f'O maior número é: {maiorNumero}')
print(f'O menor número é: {menorNumero}')