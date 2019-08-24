'''
09 - Dado um número inteiro n >= 0, calcular n!. Ex.: 5!=5.4.3.2.1=120
'''
a = 1
n = int(input("Escreva um número inteiro para calcular !: "))
while n < 0:
    n = int(input("Escreva um número positivo: "))

while n != 0:
    a = a * n
    n = n -1
print(a)
