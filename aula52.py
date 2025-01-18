'''
Tipos de tuplas Uma lista imutavel + tuples (tuplas)
Bassicamente tuplas são listas imutaveis
'''
nomes = ['joaquim', 'jorge', 'godzila']
nomes.append('osso')
nomes = list(nomes)
nomes = tuple(nomes)


print(nomes[-1])
print(nomes)