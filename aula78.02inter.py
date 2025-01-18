
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis; dic, list
# - aceitam esses valores, str, int, float, tupla
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# ----------------------------------------------
# s1 = {1,2,3,3,3,4,5,}# set eliminão valores repetidos
# print(s1)
# ===========================================
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# l1 = [1,2,3,3,3,3,3,3,4,5,6] # list de caracteres repeditos
# s1 = set(l1) # converte em um set pra tirar os repetidos
# l2 = list(s1) #converte novamente em uma list com valores unicos
# print(l1)
# print(s1)
# print(l2)
# =================================================
# - Não aceitam valores mutáveis; dic, list
# - aceitam esses valores, str, int, float, tupla
# s1 = {1,2,3,(22,3,4,4)} 
# print(s1)
# =========================================================
# # - são iteráveis (for, in, not in)
# s1 = {1,2,3,4,5}
# print(3 in s1) # verifica e return verdadeiro
# print(2 not in s1)# verifica e return false caso seja verdadeiro
# for numeros in s1: # para cada numero mostra numero ( valor do set)
#     print(numeros)

# ============================================= aula aqui
# Métodos úteis:
# add, update, clear, discard
s1 = set()# cria set vazio
s1.add('jorge')# adiciona de um em um valor no set
s1.update(('óla mundo', 1,2,3,4,5, 'todos'))# para adicionar varios valores ao set metodo updade (com ou parenteses dentro (( aqui vai o iteravel)), por que se nao ele itera nas letars e nao nos valores em se

s1.add(1)
# s1.clear()# limpa o set
s1.discard('óla mundo')# ele compara e descarta o valor igual ao do set, exemplo descarta (óla mundo)
print(s1)



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
