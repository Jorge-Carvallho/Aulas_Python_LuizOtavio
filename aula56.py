'''
split e join com list e str
split - divide uma string ( em uma list)
join - une uma string
rstrip - corta os espacos da direita
lstrip - corta os espacos da esquerda
'''
# frase = 'Olha so que, coisa interesante'
# lista_palavras = frase.split()
# print(lista_palavras)
# ========================================

# frase = 'o tempo disse para o tempo, que todo com tempo tem tempo'
# lista_de_frases = frase.split(', ')

# for i, frase in enumerate(lista_de_frases):
#     print(lista_de_frases[i])
# ==============================================

frase = '   olha so que    ,  coisa interessante           '

lista_de_frases_cruas = frase.split(',')


lista_de_frases = []
for i, frase in enumerate(lista_de_frases_cruas):
    lista_de_frases.append(lista_de_frases_cruas[i].strip())
    # print(lista_de_frases_cruas)
    # print(lista_de_frases)


print(lista_de_frases_cruas)
print(lista_de_frases)


frases_unidas = ', '.join(lista_de_frases)
frases_unidas = '-'.join(lista_de_frases) # pode ser usado como separador, iterador, ou unir strings
print(frases_unidas)
