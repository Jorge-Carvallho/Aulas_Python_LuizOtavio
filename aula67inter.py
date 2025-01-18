'''
Valores padrão para parâmetros
Ao definit uma função, os parâmetros podem 
ter valores padrão. Caso o valor não seja
enviadopara p parâmetro, o valor padrão será 
usado
Refatorar: editar seu código
'''

def soma (x, y, z=None):
    if z is not None: # caso sej apassado 3 paremetros o código entrar
        print(f'{x=} {y=} {z=}', x + y + z)
    else: # caso seka passado apenas 2 parametros o código entra aqui
        print(f'{x=} {y}', x + y )
    

soma(2,1)
soma(3,5)
soma(1,2,3)
soma(x=1,y=2,z=3)