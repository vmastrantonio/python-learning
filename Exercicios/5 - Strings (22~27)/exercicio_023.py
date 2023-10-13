# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Informe um número: "))

if num > 0 and num <= 9999:
    milhares = num // 1000 % 10
    centenas = num // 100 % 10
    dezenas = num // 10 % 10
    unidades = num // 1 % 10

    print(f"Milhar: {milhares}")
    print(f"Centena: {centenas}")
    print(f"Dezena: {dezenas}")
    print(f"Unidade: {unidades}")
else:
    print("O número informado deve ser entre 1 e 9999")