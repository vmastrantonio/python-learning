﻿def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumentar(n, p):
    return n * ((p / 100) + 1)

def diminuir(n, p):
    return n * (1 - (p/100))

def moeda(num=0, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")