'''
Higher Order Functions - Funções de ordem superior
Funçoes de primeira classe
'''
# def saudacao(msg):
#     return msg
# saudacao_2 = saudacao # apontando a variavel de fora pra a variavel da função
# print(saudacao_2('Bom dia'))


# teste de funcao chamando outra funcao
nome_informado = input('informa o nome da pessoa: ')
hora_informada  = int(input('Informa a hora atual (0 - 23):'))
def saudacao(msg):
    return msg

def pessoa(nome, hora):
    if hora < 12:
        return saudacao(f'Bom dia,{nome}')
    elif 12 <= hora < 18:
        return saudacao(f'Boa tarde,{nome}')
    else:
        return saudacao(f'Boa noite,{nome}')


print(pessoa(nome_informado, hora_informada))

# ==================================================
# nome_informado = input('Informe o nome da pessoa: ')
# hora_informada = int(input('Informe a hora atual (0 - 23): '))

# def saudacao(msg):
#     return msg

# def pessoa(nome, hora):
#     if hora < 12:
#         return saudacao(f'Bom dia, {nome}')
#     elif 12 <= hora < 18:
#         return saudacao(f'Boa tarde, {nome}')
#     else:
#         return saudacao(f'Boa noite, {nome}')

# print(pessoa(nome_informado, hora_informada))
