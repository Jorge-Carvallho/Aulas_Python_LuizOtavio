# Operadores in e not in
# Strings são iteráveis
#  0  1  2  3  4  5
#  o  t  a  v  i  o
# -6 -5 -4 -3 -2 -1 
# ===========================
# nome = 'otavio'
# # print(nome[])
# print('a' in nome) #retorna true
# print('vi' not in nome) #retorna false pois 'vi' esta em nome 
# print('--------------------')
# print(nome[-1] == 'o')
# print('t' in nome)
# =================================

nome = input('Digite seu nome')
encontrar = input('Digite oq ue deseja encontrar')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')