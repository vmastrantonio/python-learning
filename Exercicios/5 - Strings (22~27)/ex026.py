# Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição ela aprece a primeira vez.
# -> Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip()

print(f"A letra 'A' aparece {frase.count('a')} vezes na frase.")
print(f"A primeira letra 'A' fica na posição {frase.find("a") + 1}")
print(f"A ultima letra 'A' aparece na posição {frase.rfind("a") + 1}")