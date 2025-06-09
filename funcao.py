# def calcularMedia(nota1, nota2):
#     media = (nota1 + nota2)/2
#     return print(f'A média das notas é {media}')

# calcularMedia(10,9)

''' OUTRO JEITO '''
def calcularMedia(nota1, nota2):
    global media
    media = (nota1 + nota2)/2
    
calcularMedia(10,9)
print(media)