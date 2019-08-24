'''
Declare
    x, digito_atual, digito_ant, quoc: inteiro
    resp: logico
    
INICIO
    escreva("Digite o valor de x: ")
    leia(x)
    quoc <-- x
    dig_ant <-- -1
    resp <-- Falso
    enquanto quoc > 0 faça
        dig_atual <-- quoc MOD 10
        se dig_atual = dig_ant então
            resp <-- Verdadeiro
        fim_se
        quoc <-- quoc DIV 10
        dig_ant <-- dig_atual
    fim_enquanto
    se resp = Verdadeiro então
        escreva (x, " - SIM")
    senão
        escreva (x, " - Não")
    fim_se
FIM
'''
x=int(input("Digite o valor de x: "))
quoc=x
dig_ant=-1
resp=False
while quoc > 0:
    dig_atual = quoc % 10
    if dig_atual == dig_ant:
        resp=True
    quoc=quoc//10
    dig_ant=dig_atual
if resp:
    print(x, " - SIM")
else:
    print(x, " - Não")
print("FIM")
    
