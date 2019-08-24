'''
06 - Faça um programa que mostre na tela apenas os números ímpares entre 1 e
    50 (inclusive).

Defina: num, Inteiros
INICIO
	num <-- 1
	enquanto num <= 50 faça
		se num MOD 2 != 0 então
			escreva(num)
		fim_se
		num <-- num +1
	fim_enquanto
FIM
'''

num = 1
while num <= 50:
    if num % 2 != 0:
        print(num)
    num = num +1
