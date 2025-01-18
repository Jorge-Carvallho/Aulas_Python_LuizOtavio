'''
Lista de listas e seus índices
'''
salas = [
    ['maria', 'helena'],
    ['elaine', ],
    ['liuz', 'joao', 'eduarda',(0, 10, 20, 30, 40)],
    
]
# print(salas[0][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é { sala}')
    for i, aluno in enumerate(sala):
       
        print(i, aluno)
