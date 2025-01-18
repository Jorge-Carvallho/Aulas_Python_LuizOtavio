'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
'''

# x = 1

# def escopo():
#     x = 10
#     print(x)
#     def outra_funcao():
#         y = 2
#         print(x,y)


    
#     outra_funcao()
#     print(x)


# print(x)

# escopo()
# print(x)

# ==================================================
# permitindo que o x fosse editado dentro da funcao

x = 1
y=3
print(' saida 01 valor' ,x)
print('======================')
print('saida 02 valor',y)
print('======================')
def escopo():
    global x
    x = 111
    print(' saida 04 aqui ele altera o valor de x, com a varival global esta dentro da primeira função')
    print('======================================')
    
    def outra_funcao():
        global y
        y = 9
        print('saida 5 escopo de outra_funcao esses x e y estão da outra função valor', x , y)
        print('=======================================')
        print('saida 6 escopo de outra_funcao, valor ', y)
        print('========================================')
            
    outra_funcao()
    


print(' saida 03 x de fora da funcao valor ', x)
print('======================')


escopo()


print('aqui ele finaliza a variavel alterada valor', x)
print('====================================')

    # def outra_funcao():
    #         global y
    #         y = 9
    #         print(x,y)
    #         print(y)
    # print(f'{y} de y')
    # outra_funcao()
    # print(f'{x} {y} print da ')
