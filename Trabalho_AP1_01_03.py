'''
3
'''
ma=0
na=0
menor_indice=100000
cid_menor=""
maior_indice=0
cid_maior=""
tot_veiculos=0
tot_cidades=0

cod_cid=input("Código da cidade: ")
while cod_cid != "0":
    nome_cid=input("Nome da cidade: ")
    veiculos=int(input("Veículos de passeio: "))
    acidentes=int(input("Acidentes com vítimas"))
    if veiculos < 1000:
        ma= ma + acidentes
        na= na + 1

    indice=acidentes/veiculos
    if indice < menor_indice:
        menor_indice=indice
        cid_menor=nome_cid

    if indice > maior_indice:
        maior_indice=indice
        cid_maior=nome_cid

    tot_veiculos=to_veiculos+veiculos
    tot_cidades=tot_cidades+1
    cod_cid=input("Código da cidade: ")
if tot_cidades > 0:
    print("item a:", ma/na)
    print("item b:"," Menor indice: " menor_indice," Cidade: ", cid_menor," Maior indice: " maior_indice, cid_maior)
    print("item c:", tot_veiculos/tot_cidades)
    
    cod_cid=input("Código da cidade: ")
print("Fim!")
