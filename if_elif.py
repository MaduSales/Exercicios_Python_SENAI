idade = int(input('Digite sua idade: '))
assinatura = True

if idade >= 18 and assinatura:
    print('Acesso ilimitado a todo conteúdo premium')
elif idade > 18:
    print('Acesso ilimitado. Considere assinar o plano premium')
else:
    print('Acesso restrito ao conteúdo +18')