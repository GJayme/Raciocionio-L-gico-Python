'''
07 - Faça um programa que receba dois números inteiros e mostre na tela os
    números inteiros que estão no intervalo compreendido por eles, incluindo-os.

Defina: num1, num2, a, Inteiros
INICIO
	escreva ("Digite o primeiro número: ")
	leia(num1)
	escreva ("Digite o segundo número: ")
	leia (num2)
	se num1 > num2 faça
		a <-- num1 - num2
		enquanto a >= 0 faça
			escreva (num1)
			num1 <-- num1 -1
			a <-- a - 1
		fim_enquanto
	senão
		a <-- num2 - num1 faça
		enquanto a >= 0 faça
			escreva (num2)
			num2 <-- num2 -1
			a <-- a - 1
		fim_enquanto
FIM
'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    a = num1 - num2
    while a >= 0:
        print(num2)
        a = a -1
        num1 = num1 -1
if num2 > num1:
    a = num2 - num1
    while a >= 0:
        print(num2)
        a = a -1
        num2 = num2 -1
