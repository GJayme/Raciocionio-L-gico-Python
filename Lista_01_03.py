'''
03 - Faça um algoritmo que calcule a área de um triângulo, considerando a
    fórmula (base*altura)/2 . Utilize as variáveis AREA, BASE e ALTURA.

#PORTUGOL#

Defina: area, base, altura: Real
INICIO
	escreva ("Qual o tamanho da base do triângulo? ")
	leia (base)
	escreva ("Qual o tamanho da altura do triângulo?")
	leia (altura)
	area <-- (base * altura)/2
        escreva ("A área do triângulo é: ", área)
FIM


'''
altura = float(input("Digite o tamanho da altura, maior que zero: "))
while altura < 0:
    altura = float(input("Digite o tamanho da altura, maior que zero: "))
base = float(input("Digite o tamanho da base, maior que zero: "))
while base < 0:
    base = float(input("Digite o tamanho da base, maior que zero: "))
area = (base*altura)/2
print("O tamanho da area é igual a: ", area)
    
    
