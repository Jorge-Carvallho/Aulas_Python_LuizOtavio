# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# pessoa = dict(nome='jorge',sobrenome='carvalho', idade=34)
# pessoa = {
#     'nome': 'Jorge',
#     'sobrenome': 'Carvalho',
#     'idade': 34,
#     'altura': 1.79,
#     'endereço': [
#         {'rua': 'tal de tal', 'numero': 123},
#         {'rua': 'taue de taue', 'numero': 234}

#     ],
        
        
# }
# print(pessoa['endereço'])
# ============================================

# pessoas = dict(nome='jorge', sobrenome='carvalho')
# pessoa = {
#     'nome': 'jorge',
#     'sobrenome': 'carvalho',
#     'idade': 34,
#     'altura': 1.79,
#     'endereços':[
#         {'rua':'tal de tal', 'numero': 123},
#         {'rua': 'taue de taue', 'numero': 456},
        
#     ]

# }
# # print(type(pessoa))
# # print('------------')
    
# # print(f'meu nome é  {pessoa['nome']} {pessoa['sobrenome']}')
# # print(f'Tenho {pessoa['idade']}')

# # print(pessoa['nome'])
# for chaves in pessoa:
#     print(chaves,'-', pessoa[chaves])
# ===========================================
# Manipulando chave e valores em dicionários dinamicos

# pessoa = {}


# pessoa['nome'] = 'jorge carvalho'
# print(pessoa)
# -=========================== agora dinamica


pessoa = {}
chave = 'Nome'
pessoa[chave] = 'jorge carvalho'
pessoa['sobrenome'] = 'Miranda'
print(pessoa[chave])
print(pessoa)

print('----------------')


pessoa[chave] = 'Maria'
# del pessoa['sobrenome']
# print(pessoa[chave])
# print(pessoa)

# print(pessoa.get('sobrenome', 'não existe'))# caso nao coloque nada valor padrão é None
if pessoa.get('sobrenome') is None:
    print('pessoa não tem sobrenome')
else:
    print(pessoa[chave],pessoa['sobrenome'])
   







