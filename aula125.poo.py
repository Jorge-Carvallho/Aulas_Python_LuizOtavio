# aula204
#Atributos de classes


class Pessoa:
    ano_atual = 2025   # atributo no escopo da classe

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ano_nascimento  = Pessoa.ano_atual - self.idade   #forma correta e chamar nome da classe.nome do atributo para não ter erro
        return f'{self.nome } nasceu em  {ano_nascimento}'
    

        
        
p1 = Pessoa('Jorge', 36)
print(p1.get_ano_nascimento())
p2 = Pessoa('João', 19)
print(p2.get_ano_nascimento())

