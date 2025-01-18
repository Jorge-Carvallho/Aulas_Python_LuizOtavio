"""
Formatação básica de strings
s - corda
d-int
f - flutuar
.<número de dígitos>f
x ou X - Hexadecimal
(Caracteres)(><^)(quantidade)
> - Esquerda
< - Direita
^ -Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Sinalizadores de conversão - !r !s !a
"""
hexadecial = 1500
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')# 10 casas deciamis pra esquerda
print(f'{variavel: <10}.')#10 casas decimais a direita
print(f'{variavel: ^10}.')# 10 casas decinaois ao centro
print(f'{variavel:0^11}.')
print(f'{1000.87238487:0=+10,.2f}')
print(f'O hexadecimal de {hexadecial} é {hexadecial:08X}')