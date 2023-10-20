# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostra a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha_y in range(3):
    for coluna_x in range(3):
        matriz[linha_y][coluna_x] = int(input(f"Digite o valor da posição (Y={linha_y} | X={coluna_x}): "))

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()