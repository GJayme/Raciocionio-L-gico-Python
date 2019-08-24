'''
05 - Faça um programa que leia 10 números e ao final mostre apenas a soma e
    a média aritmética desses números.

#PORTUGOL#

Defina: num, contagem, soma, media, Real
INICIO
	contagem <-- 1
	soma <-- 0
	enquanto contagem <= 10 faça
		escreva("Digite o número")
		leia (num)
		soma <-- soma + num
			contagem <-- contagem +1
	fim enquanto
	media <-- soma/10
	escreva ("A média dos 10 números é: " media)
FIM
'''

contagem = 1
soma = 0
while contagem <= 10:
    num = float(input("Digite um número para somar: "))
    soma = soma + num
    contagem = contagem + 1
media = soma / 10
print ("A soma dos números foi de: ", soma, "e a média foi: ", media)
