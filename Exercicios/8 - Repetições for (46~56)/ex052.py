# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número inteiro: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")
else:
    print("Não é primo")