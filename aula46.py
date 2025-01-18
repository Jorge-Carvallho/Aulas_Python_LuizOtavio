for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    
    
    if i == 8:
        print('i agora é 8 seu else nao executará')
        break # aqui comentado o else será execultado

    for j in range(1,3):
        print(i, j)

else:
    print('for completo com sucesso! ')


