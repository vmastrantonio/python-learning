# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas e minúsculas.
# -> Quantas letras ao todo (sem considerar espaços).
# -> Quantas letras tem o primeiro nome.

nome_completo = str(input("Insira o seu nome: "))

nome  = nome_completo.split()

qtd_carac_nome = len(nome[0])
qtd_carac_sobrenome = len(nome[1])

print(f"Nome em maísculo: {nome_completo.upper()}")
print(f"Nome em minúsculo: {nome_completo.lower()}")
print(f"Numero total de caracteres: {qtd_carac_nome + qtd_carac_sobrenome}")
print(f"Numero de caracteres do primeiro nome: {qtd_carac_nome}")