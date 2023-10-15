# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

smaller = num1

if num2 < smaller:
    smaller = num2

if num3 < smaller:
    smaller = num3
    
bigger = num1

if num2 > bigger:
    bigger = num2

if num3 > bigger:
    bigger = num3
    
print(f"O menor número é o {smaller} e o maior número é o {bigger}")