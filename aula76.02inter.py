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

p1 = {
    'nome': 'jorge',
    'sobrenome': 'Miranda',
}
    
    
# print(p1['nome'])
# print(p1.get('nome', 'com get caso não exixte retorna None '))
#com método get consigo verificação de uma linha caso não tenha a chave retorna condição None ou mensagem
# ============================================================================================
                            # pop
# nome = p1.pop('nome')#pop retorna valor da chave e exclui a chave posterior
# print(nome)
# print(p1)
# =============================================================================
                            # popitem
# ultima_chave = p1.popitem()# popitem retorna em tupla a ultima chave e posterior remove
# print(ultima_chave)
# print(p1)
# ============================================================================
                                #update
p1.update({ #update metódo para atualizar, mudar e criar novas chaves
    'nome': 'Novo valor',
    'idade': 34
    
}) 
print(p1,' 01')
print('--------')
p1.update(nome = 'novo valor', idade= 30)  # também pode ser criado e atualizado da forma abaixo
print(p1, ' 02')
print('--------')

tupla = ('nome','novo valor'), ('idade', 34)# também pode ser usado dessa maneira
p1.update(tupla)
print(p1, ' 03')
# =================================================================================

