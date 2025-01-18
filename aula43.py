# Inicio de for


# texto = 'python'

# i = 0

# tamanho_string = len(texto)
# while i < tamanho_string:
#     print(texto[i], i)
#     i += 1



# senha_salva = '123123'
# senha_digitada = ''
# repeticao = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha({repeticao}x): ')
#     repeticao +=1


# print('aquele laço a cima pode ter repetições infinitas')


texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    
    
print(novo_texto + '*')


