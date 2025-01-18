# def imprimir(a,b,c):
#     print(a,b,c)

# imprimir('jorge', 'miranda', 'carvalho')
# imprimir(1,2,3)
# ==============================================

def saudacao(nome = 'Sem nome'): #se eu nao passar um valor na function ele vai usar este argumento (Sem nome)
    print(f'Olá {nome}')

saudacao('Jorge Nilson')
saudacao('maria')
saudacao()