# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

num = int(input("Digite um número: "))

antecessor = 0
atual = 1

cont = 0

while cont < num: 
    print(atual)
    antecessor, atual = atual, antecessor + atual
    cont += 1