# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

chosen = int(input("Escolha um número: "))

if chosen % 2 == 0:
    print("O número escolhido é par")
else:
    print("O número é impar.")