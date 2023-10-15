# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dolar = 5.04
carteira = int(input("Digite quanto de dinheiro você tem na carteira: "))

print(f"Com R$ {carteira:.2f}, você pode comprar U$ {carteira / dolar:.2f}")

