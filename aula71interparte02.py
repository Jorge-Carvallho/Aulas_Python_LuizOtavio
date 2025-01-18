

'''
*args empacota o que eu enivar pra função
*nome da variavel (*numeros)=> desenpacota para enviar pra função como parametros.....chamada pela função desempacota dês que esteja com *, exemplos abaixo
'''

def soma(*args):
    # print(args)
    total = 0
    for numero in args:
        total += numero
        # print(total)
    return total
        

# soma_1_2_3 =soma(1,2,3)
# print(soma_1_2_3)

# soma_4_5_6 =  soma(4,5,6)
# print(soma_4_5_6)

# soma_10_20_30 = soma(10,20,30)
# print(soma_10_20_30)

numeros = 1,2,3,4,5,6,7,8,9
outra_soma = soma(*numeros)#argumento *numeros vem desenpacotado, se usar, argumento sem desempacotar da erro pos fica uma tupla dentro de outra tupla
# print(numeros, type(numeros))
print(outra_soma)
print(numeros)#aqui esta empacotado
print(*numeros)# aqui esta desenpacotado
# passar uma quantidade de argumentos ilimitados de soma não nomeados