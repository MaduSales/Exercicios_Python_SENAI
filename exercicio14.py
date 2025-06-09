numeros = ()
cont9 = 0
numeros_pares = []
var_3 = 0

for i in range(4):
    numero = int(input(f'Digite o {i + 1}º número: '))
    numeros += (numero,)

for i, numero in enumerate(numeros):
    if numero == 9:
        cont9 += 1
    if numero == 3:
        var_3 = i
    if numero %2 == 0:
        numeros_pares.append(numero)

print(f'O número de vezes que o número 9 foi {cont9}')
print(f'O número 3 apareceu na posição {var_3}')
print(f'Os números pares são :{numeros_pares}')
    