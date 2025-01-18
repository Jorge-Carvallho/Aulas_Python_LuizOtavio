'''
Imutaveis: não pode ser atribuidos outras variáveis as ja exixtentes
str, int, float, boll
'''
string = 'Jorge Carvalho'
outra_variavel = f'{string[:4]}E{string[5:]}'
print(outra_variavel)
print(string.capitalize())
print(string.zfill(20))