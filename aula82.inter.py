
#  codigo 1  <======
# def execulta(funcao,*args):
#     return funcao(*args)

# def soma(x,y):
#     return x,y
# # 3 exemplos abaixo do def soma
# print(
    
#     execulta(
#         lambda x,y : x + y,
#         2,3
#     ),
#     # execulta(soma,2,3),
#     # soma(2, 3)
# )
# print(execulta(soma, 2,3))
# print(soma(2, 3))

# -------------------------------------------------------------

def execulta(funcao,*args):
    return funcao(args)

def criar_mulltiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
# a mesma expressão da de cima
duplica = execulta(
    lambda m: lambda n: n * m, 
    2
)
print(duplica(2))
