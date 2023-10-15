# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = int(input("Informe o preço do produto: "))
preco_desconto = preco - (preco * 0.05)

print(f"O preço do produto com 5% de desconto fica R$ {preco_desconto:.2f}")