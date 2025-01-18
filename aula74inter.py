'''
Closure e funções que retoman outras funções
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')
# print(falar_bom_dia('jorge'))
# print(falar_boa_noite('luiz'))

for nome in ['jorge', 'miranda', 'val', 'everton']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
    
    