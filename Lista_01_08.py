'''
08 - . Dados números inteiros n e k, com k >= 0, calcular n elevado a k sem
    utilizar o operador de potência. Por exemplo, dados os números 3 e 4 o seu
    programa deve escrever o número 81.

Declare n, k: INTEIRO
Inicio
	escreva("Digite o valor da base:")
	leia(n)
	escreva("Digite o valor do expoente:")
	leia(k)
	pot <--1
	enquanto k > 0 faça
		pot <--pot*n
		k <-- k - 1
	fim_enquanto
	escreva(pot)
Fim

'''

a = 1
numero = int(input("Digite um número inteiro: "))
potencia = int(input("Digite a potencia: "))

while potencia > 0:
    a = a * numero
    potencia = potencia - 1
print(a)
