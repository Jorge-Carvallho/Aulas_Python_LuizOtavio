# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis(pode ser alterado), porém aceitam apenas
# tipos imutáveis(não pode ser alterado) como valor interno.
# ========= set se parece com um dicionario mas nao tem valor, apenas chave
# Criando um set
# set(iterável) ou {1, 2, 3}

s1 = set() # set vazio
s1 = set('Luiz') #itera o valor as que são as letras
s1 = {'luis', 1,2,3} # itera por valores, dados do set, set com dados 
print(type(set()))
print(set('Luis'))
print(s1)







# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos