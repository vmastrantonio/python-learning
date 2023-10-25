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

def resumo(num, aumento=0, reducao=0):
    print("-" * 30)
    print("Resumo do valor:")
    print("-" * 30)
    print(f"Preço analisado: R$ {num}")
    print(f"Dobro do preço: R$ {dobro(num)}")
    print(f"Metade do preço: R$ {metade(num)}")
    if aumento != 0:
        print(f"{aumento}% de aumento: R$ {aumentar(num, aumento)}")
    if reducao != 0:
        print(f"{reducao}% de redução: R$ {diminuir(num, reducao)}")
    print("-" * 30)