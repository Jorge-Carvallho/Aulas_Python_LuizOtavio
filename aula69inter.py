'''
Escopo de funções em Python 
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código pode ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz a variável do escopo externo ser a mesma no escopo interno.

'''
#Do escopo interno para o externo posso acessar des de  que apenas tenha um unico escopo,ex.. se o interno nao tiver variavel x, vou buscar do mas externo, e assim vou saindo para os externo buscando o dado, mas nao posso vim do externo para o interno


# so tenho acesso de dentro para fora e não de fora para dentro
# ====================-----v------=====================
# x = 1          # 03 terceiro busca essa

# def escopo():
#     # global x
#     # x = 10       # 02 segundo busca essa
    
#     def outra_funcao():
#         # global x
#         # x = 11            ## 01 primeiro busca essa
#         y = 2
#         print(x,y)

#     outra_funcao()
#     # print(x)

# # print(x)
# escopo()

# a palavra global faz com que eu consiga modificar uma variável externa dentro do escopos internos 
# =====================================================


x = 1

def escopo():
    # global x
    x = 10
    
    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
