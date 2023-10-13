# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite o seu nome completo: ")).split()

primeiro = nome[0]
ultimo = nome[-1]

print(f"Seu primeiro nome é: {primeiro}")
print(f"Seu ultimo nome é: {ultimo}")