# aula200
# Métodos  em instâncias de classes em Python
# Hard coded - É é algo que foi escrito diretamento no co

class Carro:
    def __init__(self,nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome } está acelerando')        
        
        
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()


celta = Carro('Celta')
print(celta.nome)
celta.acelerar()