# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy
pessoa = {
    'nome': 'jorge carvalho',
    'sobrenome': 'miranda',
    int(22): 'hf',
    # 'idade': 22,
    
}
# print(pessoa.__len__())
# print(len(pessoa)) #retorna qiuantidade de uma chave
# ----------------------------------------------------------
# print(pessoa.keys())# return count de keys
# print(list(pessoa.keys()))# return keys in list
# print(tuple(pessoa.keys()))#return keys in tuple
# for chave in pessoa.keys():# return keys in count in for
#     print(chave)
# -----------------------------------------------------------
# print(list(pessoa.values()))#return values's keys
# for valor in pessoa.values():# return values in count in for
#     print(valor)
# ------------------------------------------------------------
# print(list(pessoa.items())) #return keys and values in tuple
# for chave, valor in pessoa.items():# return keys and values in list
#     print(chave, valor)
# ------------------------------------------------------------
# pessoa.setdefault('idade', 34)# define value padrão cadso nao tenha 
# print(pessoa['idade'])# chave None, valor padrão sera esse
# ----------------------------------------------------------------------
d1 = {
    'c1': 1,
    'c2': 2,
    'l1':[0,1,2],
}

# d2 = d1#significa que d2 aponta pra o mesmo dic de d1, nao atribui
#  d2['c1'] = 1000
# print(d1) -------------> mostra que alterando d2, d1 tambem é alterado
# print('---------')
# print(d2)
# ========================================================================

# d2 = d1.copy()# método de copia raza, so copia valores imutaveis:str,int,float caso tenha um valor mutavel: lista, ele nao copiara, ele vai apontar, caso atere 1 o original tambem sera alterado, mesmo tipo de cima (shallow copy) =  copia raza
# d2['c1'] = 1000
# d2['l1'][1] = 45# observe que os item mutáveis furam linkados d1 e d2 e não copyados para d2
# print(d1)
# print(d2)
# ==========================================================================

#para copia total, import copy / metodo (deepcopy) = copia profunda

d2 = copy.deepcopy(d1)
d2['l1'][1] = 9999 #foi criado com deepcopy, uma copia profunda onde os malores copiados so são alterados em d2,  d1 continua intacto
print(d1)
print(d2)