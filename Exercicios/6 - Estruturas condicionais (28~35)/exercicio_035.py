# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

num1 = int(input("Digite o comprimento da primeira reta: "))
num2 = int(input("Digite o comprimento da segunda reta: "))
num3 = int(input("Digite o comprimento da terceira reta: "))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("As três retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo.")
    