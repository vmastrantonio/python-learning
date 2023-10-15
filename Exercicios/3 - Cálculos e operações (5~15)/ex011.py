# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

larg = int(input("Informe a largura da parede: "))
alt = int(input("Informe a altura da parede: "))

area = larg * alt
tinta = area / 2

print(f"A área da parede é de {area:.2f}m², e para pintar a parede, é necessário {tinta:.2f} litros de tinta.")