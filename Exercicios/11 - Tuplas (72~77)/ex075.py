# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

tupla = (num1, num2, num3, num4)

print(f"O valor 9 apareceu {tupla.count(9)} vezes")

if 3 in tupla:
    print(f"O valor 3 apareceu na {tupla.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

print(f"Os valores pares digitados foram: ", end="")
for n in tupla:
    if n % 2 == 0:
        print(n, end=" ")