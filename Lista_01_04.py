'''
04 - Faça um programa que leia 3 números e mostre na tela o maior número.

#PORTUGOL#

Defina: num1, num2, num3, Real
INICIO
	escreva ("Digite o primeiro número: ")
	leia (num1)
	escreva ("Digite o segundo número: ")
	leia (num2)
	escreva ("Digite o terceiro número: ")
	leia (num3)
	se num 1 > num 2 e num 1 > num 3 então
		escreva ("O primeiro número é o maior")
	senão 
		se num 2 > num 1 e num 2 > num 3 então
			escreva ("O segundo número é o maior")
		senão
			escreva ("O terceiro número é o maior")
		fim_se
	fim_se
FIM
'''
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Dgite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O número 1 é o maior: ", num1 )
if num2 > num1 and num2 > num3:
    print("O número 2 é o maior: ", num2)
if num3 > num1 and num3 > num2:
    print("O número 3 é o maior:", num3)
