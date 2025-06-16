# def calcular_media(*notas):
#     for nota in notas:
#         soma += nota
#     return soma/(len(notas))

# print(calcular_media(10,90))
# print(calcular_media(10,90,8,7,6,5))


def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

preco = float(input('Digite o valor do da venda: R$ '))
desconto = float(input('Digite o valor do desconto (0% a 100%): '))
garantia = int(input('Você deseja adicionar garantia extra?\n1. Sim\n2. Não\n'))
imposto = float(input('Digite o valor do imposto sobre o produto (0% a 100%): '))

desconto /= 100
imposto /= 100

if garantia == 1:
    garantia = preco * 0.15
else:
    garantia = 0

print(preco_final(preco, desconto = desconto, garantia_extra = garantia, imposto = imposto))