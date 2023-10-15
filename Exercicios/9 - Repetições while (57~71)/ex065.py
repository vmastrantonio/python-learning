# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foram o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

Working = True

total = cont = 0

while Working:
    num = int(input("Insira um número inteiro: "))
    
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
            
        if num < menor:
            menor = num
            
    total += num
    cont += 1
    
    deseja = str(input("Quer adicionar mais um número? [ Y ] / [ N ]: ")).upper()
    
    if deseja == "N":
        Working = False
        
mediaTotal = total / cont

print(f"Você digitou {cont} números!")
print(f"A média de todos os números que você digitou é {mediaTotal}")
print(f"O maior número digitado foi {maior} e o menor foi {menor}")
