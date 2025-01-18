import random # geração de coisas aleatórias
import sys
for i in range(20): # este for aqui estou gerando autómatico 20 cpf validos 
    nove_digitos =''

    for i in range(9):
        nove_digitos += str(random.randint(0,9))
        

    contador_regressivo_1 = 10 # contador usado a frente para a multiplicação
    resultado_digito_1 = 0 # resultado sera gerado depis do calculo multiplicado e somado

    for digitos in nove_digitos:
        # print(f'{digitos} {contador_regressivo}' ) 
        resultado_digito_1 += (int(digitos) * contador_regressivo_1) # aqui é gerado o primeiro digito do calculo digitos * contador regressivo em ordem decrecente e ja somado cada resultado da multiplicacao mas soma dos resultados 1 a 1 ex... 1* 10 = 10 | 2*10 = 20 mas 10 =30
        # print(f'{digitos} * {contador_regressivo_1} += {resultado_digito_1}  ')
        digito_1 = (resultado_digito_1 * 10) % 11
        contador_regressivo_1 -= 1
        
        digito_1 = digito_1 if digito_1 <= 9 else 0
    # print(f'Primeiro digito gerado é {digito_1}')
    # print('---------------------------')

    # -------------------------------------------------calculo 2 digito-------

    # print('CPF calculo de validacão 2 digito')
        
        
        
    dez_digitos =  nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado__digito_2 = 0
    # print(f' CPF com 1 digito validado -> {dez_digitos}')

    for digitos in dez_digitos:
        resultado__digito_2 += (int(digitos) * contador_regressivo_2)
        # print(f'{digitos} * {contador_regressivo_2} += {resultado__digito_2}')
        digito_2 = (resultado__digito_2 *10) % 11
        contador_regressivo_2 -=1
        
        digito_2 = digito_2 if digito_2 <= 9 else 0
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    # print(f'Segundo digito gerado é {digito_2}')
    print(f'{nove_digitos}{digito_1}{digito_2}')
    