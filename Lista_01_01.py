'''
01 - Faça um algoritmo que leia dois numeros inteiros,efetue a adição dos dois
    valores e apresente o valor calculado.

#PORTUGOL#

Declare: a, b, soma: Inteiros
INICIO
	escreva ("Digite o primeiro número: ")
	leia (a)
	escreva ("Digite o segundo número: ")
	leia (b)
	soma <-- a + b
	escreva ("A soma do primeiro com o segundo número é: ", soma)
FIM
'''

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
soma = a + b
print(soma)
