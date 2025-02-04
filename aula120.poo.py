# aula198
# Class - classes são modelos para criar novos objetos

# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus daods internos para realizar várias ações.
# por convenção , usamos PascalCase para nomes de classes

# Atrinutos-->> Dados dentro da classe
# Metodos -->> Acções ou funções dentro da classe

# ex:
# string = 'Jorge' # str
#     # A string é uma instancia da class str
# print(string)
# print(isinstance(string,str)) #--> checa se a variavel string é a instância de alguma classe(retorna True and False) classe str neste caso

# class Pessoa:
#     ...
     
# p1 = Pessoa()   # quando chamar 0 nome da classe + () estarei criando um novo objeto ou instância ex: p1 = Pessoa()
# p1.nome = 'jorge'
# p1.sobrenome = 'Carvalho'           #ambos são objetos diferentes com atributos diferentes
                                   
# p2 = Pessoa()  # quando chamr nome da classe + () estarei criando um novo objeto ou instância ex: p2 = Pessoa()
# p2.nome = 'Miranda'
# p2.sobrenome = 'Nilson'


# print(p1.nome)
# print(p1.sobrenome)
# print('----')
# print(p2.nome)
# print(p2.sobrenome)

    # ------------------------------
# aula199   ------------->> Classe é um molde que gera novas instâncias

# self referência p1 ou minha instância p1, depois cada argumento deve ser referenciado a ele proprio, nome = nome, sobrenome = sobrenome

class Pessoa:
    def __init__(self,nome, sobrenome):  
        self.nome = nome
        self.sobrenome = sobrenome

    
p1 = Pessoa('Jorge', 'Carvalho')
# p1.nome = 'Jorge'  
# p1.sobrenome = 'Carvalho'

p2 = Pessoa('Miranda', 'Nilson')
# p1.nome = 'Miranda'
# p1.sobrenome = 'Nilson'

print(p1.nome)
print(p1.sobrenome)


print(p2.nome)
print(p2.sobrenome)