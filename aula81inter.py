# # Introdução à função lambda (função anônima de uma linha)
# # A função lambda é uma função como qualquer
# # outra em Python. Porém, são funções anônimas
# # que contém apenas uma linha. Ou seja, tudo
# # deve ser contido dentro de uma única
# # expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda','numero': 3},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira','numero':5},
#     {'nome': 'Daniel', 'sobrenome': 'Silva','numero': 12},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira','numero': 33},
#     {'nome': 'Aline', 'sobrenome': 'Souza','numero': 0},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# print(lista, 'original')
# lista_1 = sorted(lista)# esse metodo cria um uma nova lista ja ordenada sem alterar  a original dês que esteja em uma variavel como no exemplo aqui citado,   COPIA RASA     
# # sorted(lista)
# lista.sort() # esse metodo é uma copia raza, e altera lista original
# print(lista,'sort')
# print(lista_1,'sorted')
# lista.append(22)
# print(lista)
# =========================================================

# usando sort pra ordenar uma lista de dicionarios atraves do paerametro item com função

# def ordena(item):
#     # return item # --> esse return sem o parametro de ordenação ele returna o erro de ordenacao
#     return item['nome'] #maneira correta informo que a ordenacao sera pelo parametro nome, ou 'sobrenome', ou 'numero'
 
# lista.sort(key=ordena)#key é uma definicao de função que neste caso é (nome da def -> ordena)
# for item in lista:
#     print(item)
    
# #depende da ordenação da tabela unicode para a ordem acima 
   
# função lambda
# lambda=def, 1*item=parametro(), 0 2*item=na chave item[nome e a variavel com o nome como ordenação], poderia ser sobrenome, ou numero nesse exemplo da lista acima


# def exibir(lista):
#     for item in lista:
#         print(item)
    
# lista.sort(key=lambda item: item['nome'])#ordenada pelo nome
# lista1 = sorted(lista, key=lambda item: item['sobrenome'])# ordenada pelo sobrenome
# lista2 = sorted(lista, key=lambda item: item['numero'])#ordenada pelo numero



# exibir(lista)
# exibir(lista1)
# exibir(lista2)
# ============================== refazendo ========================================

# aqui abaixo estou ensinando python a ordenar minha lista
# diacordo com os parametros das chaves  que eu quiser definir seguindo tabela unicode

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda','numero': 7},
    {'nome': 'Maria', 'sobrenome': 'Oliveira','numero':4},
    {'nome': 'Daniel', 'sobrenome': 'Silva','numero': 88},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira','numero': 1},
    {'nome': 'Aline', 'sobrenome': 'Souza','numero': 20},
]


# def ordena(pessoa):
#     return pessoa['nome']
    
# lista.sort(key=ordena)


# for pessoa in lista:
#     print(pessoa)
# -----><---<>---------><----------->><-------><>------>< >

# abaixo a mesmo expresão da funcão chamada expressão lambda
# lista.sort(key=lambda pessoa: pessoa['nome'])
# for pessoa in lista:
#     print(pessoa)


# ===================================================================================

def exibir_lista(lista):
    for item in lista:
         print(item)
    print()


l1 = sorted(lista,key=lambda pessoa: pessoa['nome'])

exibir_lista(l1)



# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()
    

# l1 = sorted(lista,key=lambda pessoa: pessoa['nome'])
# l2 = sorted(lista, key=lambda pessoa: pessoa['sobrenome'])
# l3 = sorted(lista, key=lambda pessoa: pessoa['numero'])
 

# exibir(l1)
# exibir(l2)
# exibir(l3)

# sorted return nova copia raza
# sort return a lista original

