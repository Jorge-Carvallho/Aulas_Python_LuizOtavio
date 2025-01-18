'''
Desempacotamento em chamadas
de métodos e funçoẽs
# '''
# _________________________________________________________________________
# string = 'ABCD'
# lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
# tupla = 'Python', 'é', 'legal'

# # a,b,c ,*_ = lista
# # print(a,c,)

# # for  nome in lista: 
# #     print(nome, end=' ') # separador de espacos o end ou caracter que colocar
# print(*lista)
# ==========================================================================




# _____________________________________________________________
salas = [
    ['maria', 'helena'],
    ['elaine', ],
    ['liuz', 'joao', 'eduarda',(0, 10, 20, 30, 40)],
    
]

print(*salas, sep='*')# separador ou quebra de linha com \n da list