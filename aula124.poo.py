# aula203
# Mantendo estados dentro de classes

class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True
        
        
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')

        print(f'{self.nome} está parando de filmar')
        self.filmando = False
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')    
        
        
c1 = Camera('Canon')        
c1.filmar()                     # a camera que esta filmando é True , a que nao esta é False
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print('------------------')
print(' Estados diferentes')
print('------------------')

c2 = Camera('Sony')             # ele guarda o estado que é muito importante, 
c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()



