'''
Listas em Python
Tipo de listas mutáveis
Suporta varios valores de qualquer tipo
Conhecimento reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop,del clear extend, +
Create Read Update Delete
append()- adiciona item ao final da lista
pop()- Remove do final ou do indice escolhido assim(2)exemplo
insert()- adiciona um item no indice com 2 parametros primeiro indicen segundo o que vai ser adicionado (2, 'hello') exemplo
del- apaga um indice(2)exemplo
clear- limpa a lista
extende- estende a lista mas 
+ ou -, concatena  a lista
Criar, ler, alterar, apagar = lista[i](CRUD)
'''
# ==================================================
# string = 'abcd'
# #--------0-----1---------2------------3----4
# lista = [123, True, 'jorge carvalho', 1.2, []]
# lista[2] = 'Miranda'

# print(lista)
# print(lista[2],type(lista[2]))

# ===================================================

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# # print(lista[2])
# lista.append(50) # adiciona item ao final da lista
# lista.pop() # remove o último elemento da lista po adicionando o indice no ()
# print(lista)


# ====================================================


# lista = [10, 20, 30, 40]
# lista.append('jorge')
# nome = lista.pop()
# # print(lista,lista.pop())
# print(lista, nome)
# lista.append(1234)
# del lista[-1]
# lista.insert(0,5)
# print(lista)
# ==========================================================



lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c )
print(lista_a)