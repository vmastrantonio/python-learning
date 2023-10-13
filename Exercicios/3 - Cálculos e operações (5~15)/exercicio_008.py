# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

valor = int(input("Digite um valor, em metros: "))

valor_cm = valor * 100
valor_mm = valor * 1000

print(f"Valor em centímetros: {valor_cm:.2f}")
print(f"Valor em milímetros: {valor_mm:.2f}")