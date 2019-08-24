'''
01 - 
# vi: valor inicial
# r: razão da progressão aritmetica
# qt: quantidade de termos mostrados na tela

Declare:
	vi, r: real
	qt: inteiro
Inicio
	escreva("Digite o valor inicial: ")
	leia(vi)
	escreva("Digite a razão: ")
	leia(r)
	escreva("Digite a quantidade de termos: ")
	leia(qt)
	enquanto qt >= 0 faça
		escreva(vi)
		vi <-- vi + r
		qt <-- qt -1
		
	fim_enquanto
Fim
'''

vi=float(input("Digite o valor inicial:"))
r=float(input("Digite a razão da progressão aritimetica: "))
qt=int(input("Digite a quantidade de termos: "))

print("vi", vi)
print("r", r)
print("qt", qt)

while qt > 0:
    print(vi)
    vi = vi + r
    qt = qt - 1
