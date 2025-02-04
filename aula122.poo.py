# aula201
# Entendendo self em classes Python
# Classe é molde (geralmente sem dados)
#  Instância de classe (objeto) tem Dados
# Uma classe pdoe gerar varias instâncias
#  Na clase o self é a própria instância

class Carro:
    def __init__(self,nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando')
        
        
fusca = Carro('Fusca')      # aqui fusca é um objeto carro de nome Fusca
Carro.acelerar(fusca)       # class Carro acelera o objeto que sta na variavel fusca

# ou


celta = Carro('Celta')      # aqui celta é um objeto Carro de nome Celta
celta.acelerar()            # aqui carro acelera e acelerar recebe self que é a propria instância
# Carro.acelerar(celta)     #


