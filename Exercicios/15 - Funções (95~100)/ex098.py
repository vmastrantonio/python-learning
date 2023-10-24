# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        fim = fim + passo
    elif fim < inicio:
        fim = fim - passo
        passo = -passo
    else:
        fim = fim + passo

    for i in range(inicio,fim,passo):
        print(i, end=" ")
    print("FIM!")
 
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)