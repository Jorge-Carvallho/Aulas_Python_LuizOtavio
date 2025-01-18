'''
Operação ternária (condicional de uma linha)
< valor - if - <condicional> else <outro valor>
'''
# exemplo
# print('Valor' if True else 'outro valor')
# print('Valor' if False else 'outro valor')
# =======================================================

# condicao = 10 == 10

# variavel = print('valor correto ' if condicao else 'Valor incorreto')
# =========================================================

digito = int(input('digite o digito '))

novo_digito = digito if  digito <= 9 else 'maior de 9 execuolta o else aqui'
novo_digito_ternario = 'execultou ternario ' if  digito < 9  else 'deu falso' 
novo_digito_invertido = 0 if digito > 9 else 'execulta o else aqui agora'
print(novo_digito_ternario)
print(novo_digito)