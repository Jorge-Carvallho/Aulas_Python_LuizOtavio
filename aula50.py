# 1 método

# lista = ['maria', 'helena', 'luiz']
# indice = 0
# lista.append([True, False]) # adiciona 1 elemento ou uma lista dentro de outra lista
# lista.extend([2,32,False]) # adiciona varios item a uma lista de uma so vez

# for nome in lista:
#     print(indice, lista[indice], type(nome))
#     indice += 1
# ===================================================================

# 2 metodo 

lista = ['jorge', 'miranda', 'henrique']
lista.extend([1, 'carvalho', False, 1.2])
ultimo_elemento = lista.pop()

indices = range(len(lista))
print('ultimo elemento da lista retirado ',ultimo_elemento, 'no indice', len(lista))

for indice in indices:
    print(indice, lista[indice],type(lista[indice]))
                    
                    
                    
                    
                    
                    