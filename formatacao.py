texto = 'senai'
print(texto.capitalize())
# capitalize: deixa somente a primeira letra miúscula
# casefold: deixa todas as letras minúsculas

texto = 'senai@gmail.com.br'
print(texto.count('.'))
# Conta quantos caracteres existe na frase de acordo com o argumento inserido para ser contado. Aqui passamos o ponto.

print(texto.endswith('gmail.com.br'))
# Verifica se final da String está igual aos caracteres passados na função.

print(texto.find('@'))
# Mostra o índice do caractere escolhido

texto = 'Brócolisç'
print(texto.isalnum())
# Verifica se todo texto é feito de caracteres alfanuméricos (numeros ou letras)

texto = 'Brócolisç'
print(texto.isalpha())
# Verifica se todo texto é feito de caracteres alfanuméricos (numeros ou letras)

texto = 'Brócolisç'
print(texto.isnumeric())
# Verifica se todo texto é feito de caracteres numéricos