# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.l

soma = 0

for c in range(3, 500, 6):
    soma += c
    
print(f'A soma é {soma}')