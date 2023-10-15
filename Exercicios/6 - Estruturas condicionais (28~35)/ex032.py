# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

year = int(input("Digite algum ano: "))

if year % 4 == 0:
    print(f"O ano {year} é um ano bissexto!")
else:
    print(f"O ano {year}, não é um ano bissexto.")