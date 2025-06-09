def operacoes_basicas(num1, num2):
    soma = num1 + num2
    diferenca = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2
    return (soma, diferenca, mult, divisao) # <- Retorna uma tupla

# Desempacotando Tuplas
soma, sub, mult, div = operacoes_basicas(2, 2)
print(f'Soma: {soma}')