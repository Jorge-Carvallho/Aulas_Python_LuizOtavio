# exemplo de uso de dados sets
letras = set()# aqui posso criar um criador de valores set
while True:
    letra = input('Digite uma letra: ')# digita a letra e armazena em letras
    letras.add(letra.lower())# qualquer letra do usuario vira minuscula
    
    
    if 'jorge' in letras:# verifica se letra criada existe noset letras
        print('achei a palavra e saindo agora')# acha a letra e sai do programa
        break
      
    print(letras)

