# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = int(input("Digite o número de km que foram utilizados: "))

preco_dias = dias * 60
preco_km = km * 0.15

print(f"O valor total pelo aluguel do carro é de R$ {preco_dias + preco_km:.2f}")