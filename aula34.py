'''
Repetição 
While (enquanto)
Execultar uma ação enquanto uma condição for verdadeira
'''

condicao = True

while condicao:
    nome = input('Qual seu nome ')
    print(f'Nome é {nome}')

    if nome == 'Sair':
        break

print('Saindo ...')