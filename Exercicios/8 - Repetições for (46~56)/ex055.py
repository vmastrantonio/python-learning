# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

registro = []

for c in range(1, 6):
    peso = float(input("Digite o peso da pessoa: "))
    registro += [peso]
    
print('O Maior peso foi:', max(registro))
print('O Menor peso foi:', min(registro))
