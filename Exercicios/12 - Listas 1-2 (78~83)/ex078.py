# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas recpectivas posições na lista.

lista = []

for i in range(0,5):
    lista.append(int(input("Insira um numero: ")))

maior = max(lista)
menor = min(lista)

print(f"O maior valor digitado foi o {maior}, na posição {lista.index(maior)} e o menor foi o {menor}, na posição {lista.index(menor)}")