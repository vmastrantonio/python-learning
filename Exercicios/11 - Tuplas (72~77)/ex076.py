# Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("produto1", 5.00, "produto2", 10.00, "produto3", 15.00, "produto4", 20.00)

print("-" * 40)
print(f"{"Listagem de preços":^40}")
print("-" * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end="")
    else:
        print(f"R$ {produtos[pos]:>7.2f}")

print("-" * 40)