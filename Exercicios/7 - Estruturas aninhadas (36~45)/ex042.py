# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados são iguais
# - Isósceles: Dois lados são iguais
# - Escaleno: Todos os lados são diferentes

num1 = int(input("Digite o comprimento da primeira reta: "))
num2 = int(input("Digite o comprimento da segunda reta: "))
num3 = int(input("Digite o comprimento da terceira reta: "))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    if num1 == num2 == num3:
        print("É um triângulo equilátero.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")