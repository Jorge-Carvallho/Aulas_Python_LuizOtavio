# aula202
# Escopo da classe e método da classe

class Animal:
    
    def __init__(self,nome):
        self.nome = nome
        
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento} '


        
        
        
        
leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('uva'))
