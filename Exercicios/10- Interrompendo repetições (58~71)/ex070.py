# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.00
# C) Qual é o nome do produto mais barato

cont = total = produtos_caros = 0

while True:
    nome_produto = str(input("Digite o nome de um produto: "))
    preco_produto = float(input("Digite o preço desse produto: "))
    
    if cont == 0:
        nome_produto_barato = nome_produto
        preco_produto_barato = preco_produto
    elif preco_produto < preco_produto_barato:
        nome_produto_barato = nome_produto
        preco_produto_barato = preco_produto
    
    total += preco_produto
    
    if preco_produto > 1000:
        produtos_caros += 1
        
    cont += 1
    
    escolha = " "
    
    while escolha not in "SN":
        escolha = str(input("Deseja cadastrar outro produto? [S/N]: ")).strip().upper()
    
    if escolha == "N":
        break
    
print(f"Você gastou um total de R$ {total:.2f} nessa compra.")
print(f"Você comprou {produtos_caros} que custaram mais de R$ 1000,00!")
print(f"O produto mais barato que você comprou, foi um(a) {nome_produto_barato} por R$ {preco_produto_barato}")