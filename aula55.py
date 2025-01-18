import decimal

# o importe decimal funcina melhor para números float muito grandes ou calculos que pecisao ser preciso, forma mas facil de usar e convertendo um string para decial ex comentado abaixo.

# numero_1 = decimal.Decimal('0.1') # feito dessa forma não pecisa formatacao abaixo
# numero_2 = decimal.Decimal('0.7')  

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2




print(numero_3)
print(f'{numero_3:.2f}') # formate ele formata a string em float adicionando as casas decimais

print(round(numero_3,1)) # round ele arredonda o valor para float sem as próximas casas decimais