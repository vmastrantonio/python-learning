# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print("O primeiro valor é maior")
if num2 > num1:
    print("O segundo valor é maior")
else:
    print("Os dois valores são iguais")