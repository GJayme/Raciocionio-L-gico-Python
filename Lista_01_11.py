'''
11 - Elabore um algoritmo que mostre a série na tela e ao final o valor da soma
    S para cada um dos itens a seguir: 
a) S = (1/1) + (3/2) + (5/3) + (7/4) + ... + (99/50)
'''

num1 = 1
num2 = 1
soma = 0

while num1 <= 99 and num2 <= 50:
    a = num1 / num2
    print(a)
    soma = soma + a
    num1 = num1 + 2
    num2 = num2 +1
print(soma)

'''
b) S = (2^1/50) + (2^2/49) + (2^3/48) + ... + (2^50/1)
'''

num1 = 1
num2 = 50
somra = 0

while num1 <= 50 and num2 >= 1:
    
