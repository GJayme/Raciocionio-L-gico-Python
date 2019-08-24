'''
10 - Dados números inteiros n, i e j, todos maiores do que zero, imprimir em
    ordem crescente os n primeiros naturais que são múltiplos de i ou de j e
    ou de ambos. Por exemplo, para n = 6, i = 2 e j = 3 a saída deverá ser:
    0 2 3 4 6 8 --> total de 6 números
'''

a = 0 #CONTADOR DE QUANTOS MULTIPLOS FORAM IMPRESSOS#
cm = 0 #O PROXIMO A SER TESTADO#
n = int(input("Digite quantos números inteiros você quer: "))
i = int(input("Digite o primeiro multiplo: "))
j = int(input("Digite o segundo multiplo: "))

while a < n:
    if cm % i == 0 or cm % j == 0:
        print(cm)
        a = a +1
    cm = cm +1
    
