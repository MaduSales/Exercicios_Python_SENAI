def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
    except:
        raise ValueError('Email não possui @. Digite novamente.')
    else: 
        servidor = email[posicao_a:] # <- Esses dois pontos trará a informação partido do nº do index para frente
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor:
            return 'outlook'
        elif 'yahoo' in servidor:
            return 'yahoo'
        else:
            return 'Outro'
        
email = input('Digite seu email: ')
print(descobrir_servidor(email))