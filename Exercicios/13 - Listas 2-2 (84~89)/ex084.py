# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

matriz = []

while True:
    temp = []

    temp.append(input("Digite o nome da pessoa: "))
    temp.append(float(input("Digite o peso da pessoa: ")))

    if len(matriz) == 0:
        maior_peso = menor_peso = temp[1]

    elif temp[1] > maior_peso:
        maior_peso = temp[1]
    elif temp[1] < menor_peso:
        menor_peso = temp[1]

    matriz.append(temp)

    if input("Deseja continuar? [S/N] ").strip().lower() == 'n':
        break

num_pessoas = len(matriz)

print(f"Pessoas cadastradas: {len(matriz)}")

print(f"O maior peso registrado foi {maior_peso} Kgs, peso de: ", end="")
for pessoa in matriz:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end=", ")

print()

print(f"O menor peso registrado foi {menor_peso} Kgs, peso de: ", end="")
for pessoa in matriz:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end=", ")

print()