'''
Argumentos nomeados e não nomeados em funçõoes Python
Argumrnto nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

'''
def soma(x, y,z):
    #definição da função   
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2,3)
soma(1,2,3)
soma(1,z=2,y=3)

print(1,2,3, sep='-')