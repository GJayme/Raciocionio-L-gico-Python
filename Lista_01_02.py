'''
02- Faça um algoritmo para calcular a área de uma circunferência, considerando
    a fórmula ÁREA = π * RAIO^2. Utilize as variáveis AREA e RAIO,
    a constante π (pi = 3,14159) e os operadores aritméticos de multiplicação.

#PORTUGOL#

Declare: Area, pi, raio: Real
INICIO
	pi = 3,14159
	escreva ("Qual o valor do Raio da circunferência?")
	leia(raio)
	area <-- pi * (raio^2)
	escreva ("A área da circunferência é: ", area)
FIM
'''

pi = 3.14159
raio = float(input("Digite o valor do raio da circunferência: "))
while raio < 0:
    raio = float(input("Digite um valor de raio maior que zero: "))
area = pi * raio
print("A área da circunferência é: ", area)
