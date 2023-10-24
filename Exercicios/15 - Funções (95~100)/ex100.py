# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 númeors e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

from random import randint

numeros = []

def sorteio():
    print(f"Sorteando 5 valores da lista: ", end="")
    for i in range(5):
        num = randint(1,10)
        numeros.append(num)
        print(num, end=" ")
    print("FIM!")

def somaPar(lista):
    totalSoma = 0
    for n in lista:
        if n % 2 == 0:
            totalSoma += n
    print(f"Somando os valores pares de {numeros}, temos: {totalSoma}")

sorteio()
somaPar(numeros)
help(sorteio)