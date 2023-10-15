# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

cont = 0

while True:
    num = int(input("Digite um número: "))
    print('-' * 10)
    if num < 0:
        break
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 10)