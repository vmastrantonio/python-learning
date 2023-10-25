def metade(n, format=False):
    num = n / 2
    if format:
        num = moeda(num)
    return num

def dobro(n, format=False):
    num = n * 2
    if format:
        num = moeda(num)
    return num

def aumentar(n, p, format=False):
    num = n * ((p / 100) + 1)
    if format:
        num = moeda(num)
    return num

def diminuir(n, p, format=False):
    num = n * (1 - (p/100))
    if format:
        num = moeda(num)
    return num

def moeda(num=0, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")