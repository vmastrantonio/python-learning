# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = 0
soma_coluna_x = 0
maior_da_coluna_y = 0

for linha_y in range(3):
    for coluna_x in range(3):
        num = int(input(f"Digite o valor da posição [Y={linha_y}/X={coluna_x}]: "))

        matriz[linha_y][coluna_x] = num

        if num % 2 == 0:
            soma_pares += num

        if coluna_x == 2:
            soma_coluna_x += num

        if linha_y == 1:
            if coluna_x == 0:
                maior_da_coluna_y = num
            elif num > maior_da_coluna_y:
                maior_da_coluna_y = num

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()

print(f"Soma de todos valores pares digitados: {soma_pares}")
print(f"Soma de todos valores da terceira coluna: {soma_coluna_x}")
print(f"O maior número da segunda linha é: {maior_da_coluna_y}")