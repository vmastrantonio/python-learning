# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangulas (largura e comprimento) e mostra a área do terreno.

def area(larg,comp):
    area = larg * comp
    print(f"Area de um terreno {larg}x{comp} é de {area:.2f}m²")

larg = float(input("Digite a largura de um terreno: "))
comp = float(input("Digite o comprimento de um terreno: "))

area(larg,comp)
